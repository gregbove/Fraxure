import time
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])


@app.route("/time")
def get_current_time():
    return {"time": time.time()}
