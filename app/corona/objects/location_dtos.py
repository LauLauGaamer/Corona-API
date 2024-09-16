from dataclasses import dataclass, asdict
from datetime import date
from typing import Optional

from .enums import LocationTypeEnum

@dataclass
class LocationDTO:
    name: str
    id: int | str | None
    type: LocationTypeEnum

    def to_dict(self):
        data = asdict(self)
        if self.type is not None:   
            data["type"] = str(self.type)
        return data
    
    def get_api_url(self):
        return f'https://api.corona-zahlen.org/{self.type.api_str()}/{self.id}/history/cases/'


@dataclass
class DistrictDTO(LocationDTO):
    state: str 
    county: str
    
    def __init__(self, name, id, state, county):
        super().__init__(name=name, id=id, type=LocationTypeEnum.DISTRICT)
        self.state = state
        self.county = county


@dataclass
class StateDTO(LocationDTO):
    abbreviation: str

    def __init__(self, name, abbreviation):
        super().__init__(name=name, id=abbreviation, type=LocationTypeEnum.STATE)
        self.abbreviation = abbreviation

@dataclass
class TownDTO(LocationDTO):
    plz: str
    district: str
    state: str

    def __init__(self, name, plz, district, state):
        super().__init__(name=name, id=plz, type=LocationTypeEnum.TOWN)
        self.plz = plz
        self.district = district
        self.state = state
    

@dataclass
class DatapointDTO:
    endpoint_id: int | str
    endpoint_name: str
    date: date
    cases: int | None
    incidence: float | None
    deaths: int | None
    recovered: int | None
    # evt. Age Group / Männer Frauen etc.