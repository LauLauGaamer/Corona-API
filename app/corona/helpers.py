from .services.db_service import insert_all_disctricts, insert_all_states, insert_all_towns
from .services.location_service import get_all_districts, get_all_states, get_all_towns, get_location
from .objects.enums import LocationTypeEnum
from .objects.location_dtos import DistrictDTO, TownDTO, StateDTO

from typing import List

def sync_database():
    states = get_all_states()
    districts = get_all_districts()
    towns = get_all_towns()

    states = remove_double_entries(states)
    districts = remove_double_entries(districts)
    towns = remove_double_entries(towns)
    
    insert_all_states(states)
    insert_all_disctricts(districts)
    insert_all_towns(towns)

def remove_double_entries(objList: List[DistrictDTO | StateDTO | TownDTO]) -> List[DistrictDTO | StateDTO | TownDTO]:
    for obj in objList:
        try:
            db_obj = get_location(type(obj), obj)

            objList.remove(db_obj)
        except:
            continue

    return objList