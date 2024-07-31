API ENDPOINTS:

DOKU:  https://api.corona-zahlen.org/docs/endpoints/germany.html
MAIN:  https://api.corona-zahlen.org

--> /germany 
    Eine Art Übersicht über Deutschland

    --> /history
        Keine Daten nur Endpunkt für alle möglichen historischen Daten

        --> /cases(/:days)
            Gibt insgesamte Fälle für ..Tage pro Tag zurück

        --> /incidence(/:days)
            Gibt die 7-Tage-Inzidenz für die letzten ..Tage zurück

        --> /deaths(/:days)
            Gibt die Tode für die letzten ..Tage zurück

        --> /recovered(/:days)
            Gibt den Wert der genesenen der letzten ..Tage zurück

        --> /rValue(/:days)
            Gibt den R-Wert der letzten ..Tage zurück

        --> /frozen-incidence/:days


        --> /hospitalization/:days
            Verweis auf Doku --> https://api.corona-zahlen.org/docs/endpoints/germany.html#germany-history-hospitalization-days

        -->/age-groups
            Gibt Alle Werte (Getrennt Männlich/Weiblich) für die einzelnen Altersgruppen zurück

    


--> /states/:Abkürzung
    Zugriff auf Deutsche Bundesländer

--> /districts
    Zugriff auf Kreisverbände