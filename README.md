GameHub – Turnierverwaltung

Schulprojekt (LF8): Verwaltung von E-Sports-Turnieren mit Teams, Spielern, Begegnungen und Ergebnissen.

Technik: Python (Flask), zwei getrennte Docker-Container (Backend und Frontend), Datenbank SQLite.

Aufbau
gamehub/
├── docker-compose.yml
├── backend/     Flask-API (nur JSON unter /api/...), spricht mit SQLite
│   ├── app.py
│   ├── schema.sql      Tabellen + Testdaten
│   └── init_db.py      baut die DB aus schema.sql
└── frontend/    Flask-App, rendert die HTML-Seiten
    ├── app.py          holt Daten per HTTP vom Backend
    └── templates/

Das Frontend ist unter Port 5000 erreichbar. Das Backend läuft nur im internen Docker-Netzwerk (Port 5001), nur das Frontend spricht mit ihm.

Voraussetzungen
Git
Docker Desktop (unter Windows mit WSL2). Docker Desktop muss laufen, bevor du die Befehle unten ausführst.

Prüfen:

bash
git --version
docker --version
docker compose version
Starten
Repo klonen und in den Ordner wechseln:
bash
git clone <repo-url>
cd gamehub
Container bauen und starten (das erste Mal dauert ein paar Minuten):
bash
docker compose up --build

Dieses Terminal bleibt offen, hier laufen die Logs.

In einem zweiten Terminal im selben Ordner die Datenbank anlegen (nur beim ersten Mal nötig):
bash
docker compose exec backend python init_db.py
Im Browser öffnen: http://localhost:5000 Du solltest die Tabelle mit den Teams sehen.

Reihenfolge beachten: Erst Schritt 3, dann den Browser öffnen. Ohne Datenbank gibt das Backend einen Fehler zurück.

Stoppen
Container anhalten: Strg + C im Terminal mit den Logs, oder in einem anderen Terminal docker compose down
Beim nächsten Mal reicht docker compose up. Die Datenbank bleibt erhalten, init_db.py ist nicht noch einmal nötig.
Datenbank zurücksetzen

Nach Änderungen an backend/schema.sql oder wenn die Daten kaputt sind:

bash
docker compose down -v
docker compose up --build
docker compose exec backend python init_db.py

down -v löscht das Docker-Volume mit der SQLite-Datei. Das gilt nur für deinen Rechner. Wenn jemand das Schema ändert und es gemergt wird, müssen alle im Team ihre lokale DB so zurücksetzen.

Häufige Probleme
Problem	Lösung
docker: command not found oder "Cannot connect to the Docker daemon"	Docker Desktop starten und warten, bis die Engine läuft
Port 5000 ist belegt	Anderes Programm beenden oder in docker-compose.yml bei frontend den linken Wert ändern, z. B. "5050:5000"
Browser zeigt Fehlerseite	init_db.py (Schritt 3) noch nicht ausgeführt
Änderung an requirements.txt wird ignoriert	docker compose up --build erneut ausführen

Code-Änderungen in .py- und .html-Dateien werden dank Bind-Mount und Debug-Modus automatisch übernommen, ein neuer Build ist dafür nicht nötig.

Git-Workflow
main ist immer lauffähig.
Jede*r arbeitet in einem eigenen Branch, z. B. feature/teams-verwaltung.
Merge nach main nur per Pull Request, mindestens eine andere Person schaut kurz drüber.
Kleine, aussagekräftige Commits.
Die SQLite-Datei wird nicht eingecheckt (steht in der .gitignore), versioniert wird backend/schema.sql.
