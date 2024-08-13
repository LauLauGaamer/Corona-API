from typing import List
from ..dtos.location_dtos import *
from ..models import *

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
