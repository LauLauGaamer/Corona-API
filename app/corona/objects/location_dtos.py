from dataclasses import dataclass
from .enums import LocationTypeEnum

@dataclass
class DistrictDTO:
    district_id: int
    state: str 
    county: str
    name: str
    type: str = LocationTypeEnum.DISTRICT


@dataclass
class StateDTO:
    id: int
    name: str
    abbreviation: str
    type: str = LocationTypeEnum.STATE


@dataclass
class TownDTO:
    name: str
    plz: str
    district: str
    state: str
    type: str = LocationTypeEnum.TOWN