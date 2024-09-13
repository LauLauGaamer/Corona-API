from dataclasses import dataclass, asdict

from .enums import LocationTypeEnum

@dataclass
class DistrictDTO:
    district_id: int
    state: str 
    county: str
    name: str
    type: LocationTypeEnum = LocationTypeEnum.DISTRICT

    def to_dict(self):
        data = asdict(self)
        data["type"] = str(self.type)
        return data

@dataclass
class StateDTO:
    id: int
    name: str
    abbreviation: str
    type: LocationTypeEnum = LocationTypeEnum.STATE

    def to_dict(self):
        data = asdict(self)
        data["type"] = str(self.type)
        return data

@dataclass
class TownDTO:
    name: str
    plz: str
    district: str
    state: str
    type: LocationTypeEnum = LocationTypeEnum.TOWN

    def to_dict(self):
        data = asdict(self)
        data["type"] = str(self.type)
        return data