from django.conf import settings

from typing import List, Dict
from datetime import date, datetime, timedelta
import requests

from ..objects.location_dtos import LocationDTO, DatapointsDTO
from ..objects.enums import LocationTypeEnum, APIDataTypeEnum
from ..objects.exceptions import MissingDataPointError

base_dir = settings.BASE_DIR

def request_api(url: str) -> requests.Response:
    response = requests.get(url).json()
    return response

def read_file_lines(url: str = base_dir / 'corona/static/files/Liste-Staedte-in-Deutschland.csv') -> List[str]:
    with open(url, 'r', encoding = 'utf-8') as file:
        return file.readlines()
# Datei: corona/services/data_service.py:21-22   
def get_location_data(location: LocationDTO, startDay: date, endDay: date, dataType: APIDataTypeEnum) -> Dict[date, int | float | None]:
    url = location.get_api_url() + str(dataType)
    response = request_api(url)

    # check for not available Dates
    if startDay < datetime(2020, 1, 1).date():
        startDay = datetime(2020, 1, 1).date()

    if endDay > datetime.now().date():
        endDay = datetime.now().date()

    # extract data from response
    id_string = str(location.api_id)
    if len(id_string) == 4:
        id_string = "0" + id_string

    data = response["data"][id_string]["history"]

    # set key for data
    if dataType == APIDataTypeEnum.INCIDENCE:
        dataKey = "weekIncidence"
    else:
        dataKey = str(dataType)

    # format data & check date
    dataPoints: Dict[date, int | float | None] = {}

    for dataPoint in data:
        dataDay = datetime.strptime(dataPoint["date"], "%Y-%m-%dT%H:%M:%S.%fZ").date()
        if startDay <= dataDay <= endDay:
            dataPoints[dataDay] = dataPoint[dataKey]
        
    return dataPoints
    
def get_location_datapoints(location: LocationDTO, startDay: date | None = None, endDay: date | None = None) -> DatapointsDTO:

    # get all data
    cases = get_location_data(location=location, startDay=startDay, endDay=endDay, dataType=APIDataTypeEnum.CASES)
    deaths = get_location_data(location=location, startDay=startDay, endDay=endDay, dataType=APIDataTypeEnum.DEATHS)
    incidence = get_location_data(location=location, startDay=startDay, endDay=endDay, dataType=APIDataTypeEnum.INCIDENCE)
    recovered = get_location_data(location=location, startDay=startDay, endDay=endDay, dataType=APIDataTypeEnum.RECOVERED)

    # create DTO
    locationDatapoints = DatapointsDTO(
        endpoint_id = location.id,
        endpoint_name = location.name,
        endpoint_type = location.type,
        start_date = startDay,
        end_date = endDay,
        labels = None,
        cases = cases,
        deaths = deaths,
        incidence = incidence,
        recovered = recovered,
    )

    return locationDatapoints