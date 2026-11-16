import os
import sqlite3

from flask import Flask, jsonify

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "instance", "gamehub.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@app.get("/api/teams")
def get_teams():
    conn = get_db()
    rows = conn.execute("SELECT team_code, name, kuerzel FROM team").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])


@app.get("/api/spieler")
def get_spieler():
    conn = get_db()
    rows = conn.execute("SELECT spieler_id, name, team_code FROM spieler").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])
