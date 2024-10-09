# Corona-API
DD2 Project - Lauryn Dube<br>
Investierte Zeit: ~ 22h (Programmierung)

E-Mail für Rückfragen: lauryndube1@gmail.com<br>
Github-Projekt: https://github.com/LauLauGaamer/Corona-API 

## Voraussetzungen
- Python 3.10 oder höher muss installiert sein (am besten auf dem neusten Stand)!
- Django Version 5.1.1
- Requests Version 2.32.3
    --> Installation über die Requirements.txt ist möglich

- Entwickelt im/für den Chrome Browser (Design für 1920x1080p) 
    --> sollte etwas falsch aussehen bitte die Einstellungen nutzen!


## Installation

**Wichtig! Es ist empfehlenswert für die Installation der Anwendung zuvor ein virtuelles Environment anzulegen und diese zu nutzen!**
Die Installation ist manuell oder mithilfe der [Batch Datei (installation.bat)](installation.bat) möglich. Zur Installation einfach die [Batch Datei](installation.bat) ausführen oder folgende Schritte manuell durchführen.

## Manuelle Installation (ohne Batch-Datei)
### 1. Installieren der Python Bibliotheken

Um die genutzten Python Bibliotheken zu installieren ist es empfehlenswert die mitgelieferte [Requirements.txt](requirements.txt) zu verwenden. Zur Installation kann folgender Befehl genutzt werden:

```bash
pip install -r requirements.txt
```

### 2. Einrichten der Datenbank

Um die Datenbank initialisieren zu können muss man sich im [app-Ordner](/app/) befinden. Anschließend können die folgenden Befehle nacheinander ausgeführt werden.

```bash
cd app
python manage.py migrate
python manage.py makemigrations
```

**Hinweis: Dieser Schritt muss auch ausgeführt werden, sollte die Datenbank gelöscht werden!**

## Starten des Servers

Um den Server starten zu können, muss man sich innerhalb des [app-Ordners](/app/) befinden. Anschließend muss folgender Befehl ausgeführt werden:

```bash
cd app
python manage.py runserver
```

Zur Vereinfachung des Startens wurde jedoch auch eine ausführbare [Batch-Datei (start-server.bat)](start-server.bat) hinzugefügt.

## Wichtige Hinweise

### Vor der ersten Nutzung der Anwendung

Vor der ersten Nutzung der App muss die Datenbank einmal synchronisiert werden, damit diese alle nötigen Standorte beinhaltet. Dazu müssen folgende Schritte einmal ausgeführt werden

```bash
1. In der Navigationsleiste über das Einstellungsrad an der rechten Seite hovern
2. Auf den Eintrag "Datenbank synchronisieren" drücken
3. ca 5-10s warten, bis die Meldung "Datenbank wurde erfolgreich synchronisiert" erscheint.
```

### Beim Nutzen der Anwendung

Die Verwendete API (https://api.corona-zahlen.org) hat vor allem beim Abfragen der Bezirke (damit auch der Städte) eine Wartezeit von ca. 2s-3s pro Anfrage. 
Für die gesamte Ansicht müssen jedoch 4 Anfragen gemacht werden, welche dadurch beim aller ersten Mal laden ca. 10s benötigen.
Nachdem der Endpunkt das erste mal angefragt wurde, sind die Ladezeiten extrem Verkürzt und die Anfragen gehen sehr schnell.
