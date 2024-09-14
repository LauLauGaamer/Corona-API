from ..objects.location_dtos import *
from ..objects.exceptions import TooManyResultsError
from ..objects.enums import LocationTypeEnum
from ..models import *
from .data_service import *
from .db_service import filter_all_tables, get_district, get_state, get_town

from typing import List, Tuple

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
        town = TownDTO(id=None, name=line[1].strip(), plz=line[2].strip(), district=line[4].strip(), state=line[3].strip())
        datapoints.append(town)

    return datapoints

def search_for_location(query: str, max_results: int = 10) -> Tuple[List[TownDTO], List[DistrictDTO], List[StateDTO]]:
    towns, districts, states = filter_all_tables(name = query)

    # Check for length of results
    results_length = len(towns) + len(districts) + len(states)

    if results_length > max_results:
        results = {
            "towns": towns,
            "districts": districts,
            "states": states,
        }
        
        raise TooManyResultsError(results = results, max_results = max_results, results_length = results_length)

    return states, districts, towns

def get_location(type:LocationTypeEnum, query:str = None) -> TownDTO | DistrictDTO | StateDTO:
    match type:
        case LocationTypeEnum.TOWN:
            try:
                location = get_town(id=int(query))
            except ValueError:
                try:
                    location = get_town(name=query)
                except:
                    raise ValueError(f'Der angegebene Parameter "id"({query}) kann nicht zur id umgewandelt werden (Town)!')
        case LocationTypeEnum.DISTRICT:
            try:
                location = get_district(id=int(query))
            except ValueError:
                raise ValueError(f'Der angegebene Parameter "id"({query}) kann nicht zur id umgewandelt werden (District)!')
        case LocationTypeEnum.STATE:
            location = get_state(abbreviation=query)
        case _:
            raise ValueError('Der angegebene type stimmt nicht mit dem LocationTypeEnum überein! (Optionen: "TOWN", "DISTRICT", "STATE")')

    return location