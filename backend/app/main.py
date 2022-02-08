# entry point to start the backend
# starts api which receives requests from frontend

# flask version
# from flask import Flask

# app = Flask(__name__)

# @app.route('/hello/', methods=['GET', 'POST'])
# def welcome():
#     return "Hello World!"


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=105)

# fastapi version
import from fastapi import FastApi

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/flasksql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)