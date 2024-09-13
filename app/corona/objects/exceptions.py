class TooManyResultsError(Exception):
    def __init__(self, results_length: int, message: str = "Die Suche hat zu viele Ergebnisse geliefert.", max_results: int = 15, results = {}):
        self.message = message
        self.max_results = max_results
        self.results_length = results_length
        self.results = results

        super().__init__(self.message)

    def __str__(self):
        return f"Die Suche hat zu viele Ergebnisse geliefert. Maximal Erlaubt sind: {self.max_results} (Deine Ergebnisse: {self.results_length})"
    
class MissingParameterError(Exception):
    pass