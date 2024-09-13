from enum import Enum

class LocationTypeEnum(Enum):
    TOWN = "Town"
    DISTRICT = "District"
    STATE = "State"

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