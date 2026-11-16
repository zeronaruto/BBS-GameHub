import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
DB_PATH = os.path.join(INSTANCE_DIR, "gamehub.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")

os.makedirs(INSTANCE_DIR, exist_ok=True)

if os.path.exists(DB_PATH):
    print(f"Datenbank existiert bereits: {DB_PATH} (nichts geändert)")
else:
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema = f.read()

    conn = sqlite3.connect(DB_PATH)
    conn.executescript(schema)
    conn.commit()
    conn.close()

    print(f"Datenbank angelegt: {DB_PATH}")
