from typing import List, Tuple
from django.db.models import Q

from ..objects.location_dtos import *
from ..objects.exceptions import MissingParameterError
from ..models import *

def insert_all_states(states: List[StateDTO]):
    for stateDto in states:
        state = States(id = stateDto.id, name = stateDto.name, abbreviation = stateDto.abbreviation)
        state.save()

def get_state(id:int = None, abbreviation:str = None) -> StateDTO:
    if id is not None:
        state = States.objects.get(id = id)
    elif abbreviation is not None:
        state = States.objects.get(abbreviation__iexact=abbreviation)
    else:
        MissingParameterError("Mindestens einer der Parameter müssen gesetzt weden, um eine Datenbankabfrage (State) zu machen.")

    return StateDTO(id = state.id, name = state.name, abbreviation = state.abbreviation)
    

def insert_all_disctricts(districts: List[DistrictDTO]):
    for districtDto in districts:
        if not Districts.objects.filter(name = districtDto.name).exists():
            state = States.objects.get(name = districtDto.state)

            district = Districts(id = districtDto.district_id, state = state, county = districtDto.county, name = districtDto.name)
            district.save()

def get_district(id:int = None, name:str = None) -> DistrictDTO:
    if id is not None:
        district = Districts.objects.get(id = id)
    elif name is not None:
        district = Districts.objects.get(name__iexact=name)
    else:
        MissingParameterError("Mindestens einer der Parameter müssen gesetzt weden, um eine Datenbankabfrage (District) zu machen.")

    return DistrictDTO(district_id = district.id, name = district.name, county = district.county, state = district.state)

def insert_all_towns(towns: List[TownDTO]):
    for townDto in towns:
        state = States.objects.get(name = townDto.state)
        if Districts.objects.filter(name = townDto.name).exists():
            district = Districts.objects.get(name = townDto.name)
        else:
            district = Districts.objects.get(name = townDto.district)

        town = Towns(name = townDto.name, plz = townDto.plz, district = district, state = state)
        town.save()

def get_town(id:int = None, name:str = None) -> TownDTO:
    if id is not None:
        town = Towns.objects.get(id = id)
    elif name is not None:
        town = Towns.objects.get(name__iexact=name)
    else:
        MissingParameterError("Mindestens einer der Parameter müssen gesetzt weden, um eine Datenbankabfrage (Town) zu machen.")

    return TownDTO(plz = town.plz, name = town.name, district = town.district, state = town.state)

def filter_all_tables(name: str) -> Tuple[List[TownDTO], List[DistrictDTO], List[StateDTO]]:
    towns = Towns.objects.filter(Q(name__icontains=name) | Q(plz__icontains=name)).all()
    districts = Districts.objects.filter(name__icontains=name).all()
    states = States.objects.filter(name__icontains=name).all()
    
    # Convert into Lists of DTOs
    towns = [TownDTO(x.name, x.plz, x.district.name, x.state.name) for x in towns]
    districts = [DistrictDTO(x.id, x.state.name, x.county, x.name) for x in districts]
    states = [StateDTO(x.id, x.name, x.abbreviation) for x in states]

    return towns, districts, states