from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse

from datetime import timedelta, datetime

from corona.helpers import sync_database
from corona.services.location_service import search_for_location, get_location
from corona.services.data_service import get_location_datapoints
from corona.objects.exceptions import TooManyResultsError
from corona.objects.enums import LocationTypeEnum


# Create your views here.

def index(request):
    return HttpResponse("Hello, World. Das ist die Corona View")

def home_view(request):
    context = {
        "sync_function": sync_database,
        "navbarSearch": False,
        }
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

    context["navbarSearch"] = True
    return render(request, "pages/search.html", context)

def details_view(request, name):
    locationType = request.GET.get("type", "").lower().strip()

    try:
        typeEnum = LocationTypeEnum.from_string(locationType)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    
    # get Database entry
    locationObj = get_location(typeEnum, query=name)
    
    # Datum aus Frontend holen und ANPASSEN!
    startday = datetime.now().date() - timedelta(days=20)
    days = 14

    # get Data from API
    data = get_location_datapoints(location=locationObj, days=days, startDay=startday)

    context = {
        "navbarSearch": True,
        "data": data,
    }
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
                "towns": [town.to_dict() for town in towns],
                "districts": [district.to_dict() for district in districts],
                "states": [state.to_dict() for state in states],
                "querySucceeded": True,
            }

        except TooManyResultsError as e:
            results = {"towns": [x.to_dict() for x in e.results["towns"][:3]], "districts":  [x.to_dict() for x in e.results["districts"][:3]], "states":  [x.to_dict() for x in e.results["states"][:3]], "querySucceeded": False,}
    else:
        results = {"towns": [], "districts": [], "states": [], "querySucceeded": True}

    return JsonResponse(results)