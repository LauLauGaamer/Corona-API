from .services.db_service import *
from .services.location_service import *

def sync_database():
    states = get_all_states()
    districts = get_all_districts()
    towns = get_all_towns()
    
    insert_all_states(states)
    insert_all_disctricts(districts)
    insert_all_towns(towns)