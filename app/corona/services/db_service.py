from typing import List, Tuple
from django.db.models import Q

from ..objects.location_dtos import *
from ..objects.exceptions import MissingParameterError, MissingDatabaseEntry
from ..models import *

def insert_all_states(states: List[StateDTO]):
    for stateDto in states:
        state = States(id = stateDto.id, name = stateDto.name, abbreviation = stateDto.abbreviation)
        state.save()

def get_state(abbreviation:str) -> StateDTO:
    if abbreviation is not None:
        try:
            state = States.objects.get(abbreviation__iexact=abbreviation)
        except:
            raise MissingDatabaseEntry(f'{abbreviation} existiert in States nicht.')

    return StateDTO(name = state.name, abbreviation = state.abbreviation)
    

def insert_all_disctricts(districts: List[DistrictDTO]):
    for districtDto in districts:
        if not Districts.objects.filter(name = districtDto.name).exists():
            state = States.objects.get(name = districtDto.state)

            district = Districts(id = districtDto.id, state = state, county = districtDto.county, name = districtDto.name)
            district.save()

def get_district(id:int = None, name:str = None) -> DistrictDTO:
    if id is not None:
        try:
            district = Districts.objects.get(id = id)
        except:
            raise MissingDatabaseEntry(f'{id} existiert in Districts nicht.')
    elif name is not None:
        try:
            district = Districts.objects.get(name__iexact=name)
        except:
            raise MissingDatabaseEntry(f'{name} existiert in Districts nicht.')
    else:
        MissingParameterError("Mindestens einer der Parameter müssen gesetzt weden, um eine Datenbankabfrage (District) zu machen.")

    return DistrictDTO(id = district.id, name = district.name, county = district.county, state = district.state)

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
        try:
            town = Towns.objects.get(plz = id)
        except:
            raise MissingDatabaseEntry(f'{id} existiert in Towns nicht.')
    elif name is not None:
        try:
            town = Towns.objects.get(name__iexact=name)
        except:
            raise MissingDatabaseEntry(f'{name} existiert in Towns nicht.')
    else:
        MissingParameterError("Mindestens einer der Parameter müssen gesetzt weden, um eine Datenbankabfrage (Town) zu machen.")

    return TownDTO(plz = town.plz, name = town.name, district = town.district, state = town.state)

def filter_all_tables(name: str) -> Tuple[List[TownDTO], List[DistrictDTO], List[StateDTO]]:
    towns = Towns.objects.filter(Q(name__icontains=name) | Q(plz__icontains=name)).all()
    districts = Districts.objects.filter(name__icontains=name).all()
    states = States.objects.filter(name__icontains=name).all()
    
    # Convert into Lists of DTOs
    towns = [TownDTO(name=x.name, plz=x.plz, district=x.district.name, state=x.state.name) for x in towns]
    districts = [DistrictDTO(id=x.id, state=x.state.name, county=x.county, name=x.name) for x in districts]
    states = [StateDTO(name=x.name, abbreviation=x.abbreviation) for x in states]

    return towns, districts, states