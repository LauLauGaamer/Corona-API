from typing import List, Tuple
from dataclasses import asdict

from ..objects.location_dtos import *
from ..objects.exceptions import TooManyResultsError
from ..models import *

from django.db.models import Q

def insert_all_states(states: List[StateDTO]):
    for stateDto in states:
        state = States(id = stateDto.id, name = stateDto.name, abbreviation = stateDto.abbreviation)
        state.save()

def insert_all_disctricts(districts: List[DistrictDTO]):
    for districtDto in districts:
        if not Districts.objects.filter(name = districtDto.name).exists():
            state = States.objects.get(name = districtDto.state)

            district = Districts(id = districtDto.district_id, state = state, county = districtDto.county, name = districtDto.name)
            district.save()

def insert_all_towns(towns: List[TownDTO]):
    for townDto in towns:
        state = States.objects.get(name = townDto.state)
        if Districts.objects.filter(name = townDto.name).exists():
            district = Districts.objects.get(name = townDto.name)
        else:
            district = Districts.objects.get(name = townDto.district)

        town = Towns(name = townDto.name, plz = townDto.plz, district = district, state = state)
        town.save()

def search_for_location(query: str, max_results: int = 10) -> Tuple[List[TownDTO], List[DistrictDTO], List[StateDTO]]:
    towns = Towns.objects.filter(Q(name__icontains=query) | Q(plz__icontains=query)).all()
    districts = Districts.objects.filter(name__icontains=query).all()
    states = States.objects.filter(name__icontains=query).all()
    
    # Convert into Lists of DTOs
    towns = [TownDTO(x.name, x.plz, x.district.name, x.state.name) for x in towns]
    districts = [DistrictDTO(x.id, x.state.name, x.county, x.name) for x in districts]
    states = [StateDTO(x.id, x.name, x.abbreviation) for x in states]

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