from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from dataclasses import asdict

from corona.helpers import sync_database
from corona.services.db_service import search_for_location
from corona.objects.exceptions import TooManyResultsError

# Create your views here.

def index(request):
    return HttpResponse("Hello, World. Das ist die Corona View")

def home_view(request):
    context = {"sync_function": sync_database}
    return render(request, "pages/home.html", context)

def search_view(request):
    query = request.GET.get("q", "").lower().strip()

    # Get all Query results
    try:
        states, districts, towns = search_for_location(query, max_results=15)
        results = states + districts + towns
        results = sorted(results, key=lambda d: d.name)

        context = {
            "query": query,
            "querySucceeded": True,
            "results": results,
        }
        
    except TooManyResultsError:
        context = {
            "query": query,
            "querySucceeded": False,
            "results": [],
        }

    return render(request, "pages/search.html", context)

def details_view(request, name=None):
    context = {}
    return render(request, "pages/details.html", context)


# Backend

def sync_database_view(request):
    messages.success(request, "Synchronisierung erfolgreich abgeschlossen.")
    
    sync_database()
    return redirect("home")

def live_search(request):
    query = request.GET.get("q", "").lower().strip()
    if query:
        try:
            states, districts, towns = search_for_location(query, max_results=10)

            results = {
                "towns": [asdict(town) for town in towns],
                "districts": [asdict(district) for district in districts],
                "states": [asdict(state) for state in states],
                "querySucceeded": True,
            }

        except TooManyResultsError as e:
            results = {"towns": [asdict(x) for x in e.results["towns"][:3]], "districts":  [asdict(x) for x in e.results["districts"][:3]], "states":  [asdict(x) for x in e.results["states"][:3]], "querySucceeded": False,}
    else:
        results = {"towns": [], "districts": [], "states": [], "querySucceeded": True}

    return JsonResponse(results)