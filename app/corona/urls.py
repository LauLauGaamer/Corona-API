from django.urls import path
from .views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("backend/sync-database", sync_database_view, name="sync_database"),
]