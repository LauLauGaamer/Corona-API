from ..dtos.location_dtos import *
from typing import List
from .data_service import *

def get_all_districts() -> List[DistrictDTO]:
    datapoints = []

    request_data = request_api("https://api.corona-zahlen.org/districts")

    for id, data in request_data["data"].items():
        district = DistrictDTO(district_id=id, state=data["state"], county=data["county"], name=data["name"])
        datapoints.append(district)

    return datapoints

def get_all_states() -> List[StateDTO]:
    datapoints = []

    request_data = request_api("https://api.corona-zahlen.org/states")

    for abbreviation, data in request_data["data"].items():
        state = StateDTO(id=data["id"], name=data["name"], abbreviation=abbreviation)
        datapoints.append(state)

    return datapoints

def get_all_towns() -> List[TownDTO]:
    datapoints = []

    lines = read_file_lines()

    for line in lines:
        line = line.strip().split(";")
        town = TownDTO(name=line[1].strip(), plz=line[2].strip(), district=line[4].strip(), state=line[3].strip())
        datapoints.append(town)

    return datapoints