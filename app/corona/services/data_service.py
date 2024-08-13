import requests
from django.conf import settings

base_dir = settings.BASE_DIR

def request_api(url):
    response = requests.get(url).json()
    return response

def read_file_lines(url = base_dir / "corona/static/files/Liste-Staedte-in-Deutschland.csv"):
    with open(url, "r", encoding = "utf-8") as file:
        return file.readlines()