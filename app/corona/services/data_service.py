from django.conf import settings

from typing import List
import requests

from ..objects.location_dtos import *
from ..objects.enums import LocationTypeEnum

base_dir = settings.BASE_DIR

def request_api(url) -> requests.Response:
    response = requests.get(url).json()
    return response

def read_file_lines(url = base_dir / 'corona/static/files/Liste-Staedte-in-Deutschland.csv') -> List[str]:
    with open(url, 'r', encoding = 'utf-8') as file:
        return file.readlines()
    
def get_cases(location: StateDTO | TownDTO | DistrictDTO, days: int | None =None) -> List[DatapointDTO]:
    pass