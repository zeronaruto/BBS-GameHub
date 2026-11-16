# GameHub – Turnierverwaltung

Technikwahl: Python (Flask), zwei getrennte Container – Backend (JSON-API) und Frontend (HTML-Seiten). Datenbank: SQLite, als Datei im Backend-Container.

## Aufbau

- **backend/** – Flask-App, liefert nur JSON über `/api/...`, spricht direkt mit SQLite
- **frontend/** – Flask-App, rendert HTML-Seiten, holt sich die Daten per HTTP-Request vom Backend (`requests`-Bibliothek)

## Start (jedes Teammitglied, lokal)

```bash
git clone <repo-url>
cd gamehub
docker compose up --build
```

App läuft  auf `http://localhost:5000` (Frontend). Das Backend läuft im selben Docker-Netzwerk auf Port 5001, ist aber nicht direkt vom Host aus erreichbar – nur das Frontend spricht mit ihm.

Datenbank einmalig anlegen (Backend-Container):

```bash
docker compose exec backend python init_db.py
```

Die SQLite-Datei liegt im Docker-Volume `gamehub_data` und bleibt zwischen Neustarts erhalten. Zum Zurücksetzen: `docker compose down -v` (löscht das Volume), danach `init_db.py` erneut ausführen.

## Git-Workflow

- **main** ist immer lauffähig.
- Jede*r arbeitet in einem eigenen Branch (z. B. `feature/teams-verwaltung`), Merge nur per Pull Request mit Review.
- Kleine, aussagekräftige Commits.
