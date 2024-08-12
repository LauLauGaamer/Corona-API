import requests

def request_api(url):
    response = requests.get(url).json()
    return response

def read_file_lines(url = ".../static/files/Liste-Staedte-in-Deutschland.csv"):
    with open(url, "r") as file:
        return file.readlines()