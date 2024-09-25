from dataclasses import dataclass, asdict
from typing import Optional, Dict
import datetime

from .enums import LocationTypeEnum

@dataclass
class LocationDTO:
    name: str
    id: int | str | None
    type: LocationTypeEnum
    api_id: str

    def to_dict(self):
        data = asdict(self)
        if self.type is not None:   
            data["type"] = str(self.type)
        return data
    
    def get_api_url(self):
        return f'https://api.corona-zahlen.org/{self.type.api_str()}/{self.api_id}/history/'


@dataclass
class DistrictDTO(LocationDTO):
    state: str 
    county: str
    
    def __init__(self, name, id, state, county):
        super().__init__(name=name, id=id, type=LocationTypeEnum.DISTRICT, api_id = id)
        self.state = state
        self.county = county


@dataclass
class StateDTO(LocationDTO):
    abbreviation: str

    def __init__(self, name, abbreviation):
        super().__init__(name=name, id=abbreviation, type=LocationTypeEnum.STATE, api_id = abbreviation)
        self.abbreviation = abbreviation


@dataclass
class TownDTO(LocationDTO):
    plz: str
    district: str
    state: str

    def __init__(self, name, plz, district, state):
        super().__init__(name=name, id=plz, type=LocationTypeEnum.TOWN, api_id = district)
        self.plz = plz
        self.district = district
        self.state = state
    

@dataclass
class DatapointsDTO:
    endpoint_id: int | str
    endpoint_name: str
    start_date: datetime.date
    end_date: datetime.date
    labels: str | None
    cases: Dict[datetime.date, int | None]
    incidence: Dict[datetime.date, float | None]
    deaths: Dict[datetime.date, int | None]
    recovered: Dict[datetime.date, int | None]
    # evt. Age Group / Männer Frauen etc.

    def to_dict(self):
        return {
            'endpoint_id': self.endpoint_id,
            'endpoint_name': self.endpoint_name,
            'start_date': self.start_date.isoformat(), 
            'end_date': self.end_date.isoformat(),
            'labels': self.labels,
            'cases': {date.strftime('%d.%m.%Y'): value for date, value in self.cases.items()},
            'incidence': {date.strftime('%d.%m.%Y'): value for date, value in self.incidence.items()},
            'deaths': {date.strftime('%d.%m.%Y'): value for date, value in self.deaths.items()},
            'recovered': {date.strftime('%d.%m.%Y'): value for date, value in self.recovered.items()}
        }
    
    def generate_labels(self):
        if self.cases is not None:
            self.labels = [d.strftime('%d.%m.%Y') for d in self.cases.keys()]