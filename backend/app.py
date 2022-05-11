import time
import os
import stat
from flask import Flask
from flask_cors import CORS
from sectagtog.secUtagtog import SECTagTog

app = Flask("fraxure_backend")
CORS(app, origins=["http://localhost:3000"])
s = ''


@app.route("/")
def get_cu():
    return {"time": time.time()}


@app.route("/time")
def get_current_time():
    return {"time": time.time()}

@app.route("/tagtog/init/<ttusername>/<ttpassword>/<projname>/<form_type>/<ticker>")
def together(ttusername, ttpassword, projname, form_type, ticker): 

    s = SECTagTog(ttusername, ttpassword, "/Users/gregbove/Desktop/New_Fraxure/Fraxure/", "new.html", projname)
    s.mostRecent(form_type, ticker)
    return {"username": ttusername, "password": ttpassword, "project": projname, "form_type": form_type, "CIK": ticker}

@app.route("/tagtog/init/<ttusername>/<ttpassword>/<projname>")
def init_tagtog(ttusername, ttpassword, projname):
    s = SECTagTog(ttusername, ttpassword, " ", projname)
    return {"username": ttusername, "password": ttpassword, "project": projname}


@app.route("/tagtog/post/<form_type>/<ticker>")
def post_tagtog(form_type, ticker):
    s.mostRecent(form_type, ticker)
    return {"form_type": form_type, "CIK": ticker}

@app.route("/tagtog/init/<ttusername>/<ttpassword>/<projname>/<form_type>/<ticker>/<pre>/<post>/<yORn>")
def withDates(ttusername, ttpassword, projname, form_type, ticker, pre, post, yORn): 
    cwd = os.getcwd()
    print("Directory: " + cwd)  
    s = SECTagTog(ttusername, ttpassword, cwd, "new.html", projname)
    s.allBetween(form_type, ticker, pre, post, yORn)
    return {"username": ttusername, "password": ttpassword, "project": projname, "form_type": form_type, "CIK": ticker, "before": pre, "after": post, "directory": cwd}