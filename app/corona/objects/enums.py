from enum import Enum

class LocationTypeEnum(Enum):
    TOWN = "Stadt"
    DISTRICT = "Landkreis"
    STATE = "Bundesland"

    def __str__(self):
        return self.value
    
    @classmethod
    def from_string(cls, string_value):
        if string_value.strip() == "" or string_value is None:
            raise ValueError('Bitte gebe einen Typen als LocationTypeEnum an!')

        for name in cls:
            if name.value.lower() == string_value.lower().strip():
                return name
            
        raise ValueError(f'{string_value} ist kein Gültiger Wert für LocationTypeEnum!')
    
    def api_str(self):
        match self:
            case LocationTypeEnum.TOWN:
                return "districts"
            case LocationTypeEnum.DISTRICT:
                return "districts"
            case LocationTypeEnum.STATE:
                return "states"
            
class APIDataTypeEnum(Enum):
    CASES = "cases"
    DEATHS = "deaths"
    INCIDENCE = "incidence"
    RECOVERED = "recovered"

    def __str__(self) -> str:
        return self.value