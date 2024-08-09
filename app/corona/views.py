from django.shortcuts import render
from django.http import HttpResponse
from corona.models import * 
import requests

# Create your views here.

def index(request):
        return HttpResponse("Hello, World. Das ist die Corona View")

def home(request):
    context = {}
    return render(request, "home.html", context)

def init_database(request):
    # Muss noch vervollständigt werden!
    url = "https://api.corona-zahlen.org/states"
    response = requests.get(url).json()

    for state, data in response["data"].items():
        new_state = States(id=data["id"], name=data["name"], abbreviation=state)
        new_state.save() 

    url = "https://api.corona-zahlen.org/districts"
    response = requests.get(url).json()

    for ags, data in response["data"].items():
        new_county = County(name="county",)