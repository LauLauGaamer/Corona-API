from django.urls import path
from .views import *

urlpatterns = [
    #Main Pages
    path("", home_view, name="home"),
    path("search/", search_view, name="search"),
    path("details/<str:name>", details_view, name="details"),

    # Backend
    path("backend/sync-database", sync_database_view, name="sync_database"),
    path("backend/live-search/", live_search, name="live-search")
]