from datetime import datetime
from flask import Flask, render_template
from . import app

@app.route("/api/client")
def get_data():
    return app.send_static_file("data.json")
