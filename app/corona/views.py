from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

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