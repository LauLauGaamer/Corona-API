from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages

from corona.helpers import sync_database
from corona.services.db_service import search_for_location

# Create your views here.

def index(request):
    return HttpResponse("Hello, World. Das ist die Corona View")

def home_view(request):
    context = {"sync_function": sync_database}
    return render(request, "pages/home.html", context)

def sync_database_view(request):
    context = {}
    messages.success(request, 'Synchronisierung erfolgreich abgeschlossen.')
    

    sync_database()
    return redirect("home")

def live_search(request):
    query = request.GET.get('q', '').lower().strip()
    if query:
        states, districts, towns = search_for_location(query)

        results = {
            'towns': list(towns.values('name', 'plz')),
            'districts': list(districts.values('name')),
            'states': list(states.values('name')),
        }
    else:
        results = {'towns': [], 'districts': [], 'states': []}

    return JsonResponse(results)