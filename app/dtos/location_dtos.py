from dataclasses import dataclass

@dataclass
class DistrictDTO:
    district_id: int
    state: str 
    county: str
    name: str


@dataclass
class StateDTO:
    id: int
    name: str
    abbreviation: str


@dataclass
class TownDTO:
    name: str
    plz: str
    districts: str
    states: str