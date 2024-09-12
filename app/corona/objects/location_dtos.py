from dataclasses import dataclass

@dataclass
class DistrictDTO:
    district_id: int
    state: str 
    county: str
    name: str
    type: str = "Landkreis"


@dataclass
class StateDTO:
    id: int
    name: str
    abbreviation: str
    type: str = "Bundesland"


@dataclass
class TownDTO:
    name: str
    plz: str
    district: str
    state: str
    type: str = "Stadt"