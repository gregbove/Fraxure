import time
from flask import Flask
from flask_cors import CORS

from sectagtog.sec_tagtog import SECTagTog

app = Flask("fraxure_backend")
CORS(app, origins=["http://localhost:3000"])
s = SECTagTog()


@app.route("/time")
def get_current_time():
    return {"time": time.time()}


@app.route("/tagtog/init/<ttusername>/<ttpassword>")
def init_tagtog(ttusername, ttpassword, projname):
    s = SECTagTog(ttusername, ttpassword, "/", projname)


@app.route("/tagtog/post/<form_type>/<ticker>")
def post_tagtog(form_type, ticker):
    s.mostRecent(form_type, ticker)
