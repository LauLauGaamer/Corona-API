from datetime import date
from .enums import LocationTypeEnum

class TooManyResultsError(Exception):
    def __init__(self, results_length: int, message: str = "Die Suche hat zu viele Ergebnisse geliefert.", max_results: int = 15, results = {}):
        self.message = message
        self.max_results = max_results
        self.results_length = results_length
        self.results = results

        super().__init__(self.message)

    def __str__(self):
        return f"Die Suche hat zu viele Ergebnisse geliefert. Maximal Erlaubt sind: {self.max_results} (Deine Ergebnisse: {self.results_length})"
    
class MissingDataPointError(Exception):
    def __init__(self, start_day: date, end_day: date, missing_day: date, message:str = f"Es wurde ein fehlender Datenpunkt innerhalb der Daten festgestellt!"):
        self.message = message
        self.start_day = start_day
        self.end_day = end_day
        self.missing_day = missing_day

        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Es wurde ein fehlender Datenpunkt (Tag: {self.missing_day}) innerhalb der angefragten Punkte gefunden! (Zeitraum: {self.start_day} - {self.end_day})"

class MissingDatabaseEntryError(Exception):
    def __init__(self, key: str | int, table: LocationTypeEnum, message="Ein Eintrag wurde nicht in einer Tabelle gefunden!"):
        self.message = message
        self.key = key
        self.table = table

        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Der Eintrag {self.key} existiert in {self.table} nicht.'"
    

class MissingParameterError(Exception):
    pass