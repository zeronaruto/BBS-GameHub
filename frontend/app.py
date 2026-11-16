import os

import requests
from flask import Flask, render_template

app = Flask(__name__)

BACKEND_URL = os.environ.get("BACKEND_URL", "http://backend:5001")


@app.get("/")
def index():
    teams = requests.get(f"{BACKEND_URL}/api/teams").json()
    return render_template("index.html", teams=teams)
