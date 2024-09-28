# Corona-API
DD2 Project - Lauryn Dube

Github-Projekt: 

WICHTIG:
    - Python 3.10 oder höher muss installiert sein (am besten auf dem neusten Stand)!
    - Entwickelt im Chrome Browser (Design für 1920x1080 -> evt. nicht ganz responsible) 
        --> sollte etwas falsch aussehen bitte die Einstellungen nutzen!

Investierte Zeit: ~ 22h (Programmierung)

Was muss installiert werden:
    - python 3.11.9
    - Django vers 5.1.1
    - requests

    --> requirements.txt ist auch vorhanden

Vor dem starten des Servers st(Zugriff auf die manage.py) MUSS sicher gestellt werden, dass man im Ordner app ist (Überordner von app & Corona) (Indem die manage.py auch platziert ist)

Vor 1. Start & beim löschen der Datenbank Datei:
    - python manage.py migrate
    - python manage.py makemigrations
    - nach server Start Datenbank in der App Synchronisieren

Zum Start:
    - python manage.py runserver

Hinweise für die erste Benutzung der App:
    - Datenbank wird nicht bei jedem Serverstart automatisch gefüllt
        --> beim ersten Start: rechts oben in der Navbar über die Einstellungen Hovern und "Datenbank synchronisieren drücken"
        --> Dauert ca 5-10s, anschließend ist die App vollständig nutzbar
    - Beim ersten Anfragen eines Standortes in der API (https://api.corona-zahlen.org) kann es von der API Seite aus zu längeren Wartezeiten kommen (ca 10s)