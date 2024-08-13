from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.db.models import Q

from corona.models import *
from corona.helpers import sync_database

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
        towns = Towns.objects.filter(Q(name__icontains=query) | Q(plz__icontains=query))[:5]
        districts = Districts.objects.filter(name__icontains=query)[:5]
        states = States.objects.filter(name__icontains=query)[:5]

        results = {
            'towns': list(towns.values('name', 'plz')),
            'districts': list(districts.values('name')),
            'states': list(states.values('name')),
        }
    else:
        results = {'towns': [], 'districts': [], 'states': []}

    return JsonResponse(results)