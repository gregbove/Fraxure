# https://towardsdatascience.com/build-deploy-a-react-flask-app-47a89a5d17d9

from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/")
def api_route():
    return "this accesses the api"


if __name__ == "__main__":
    app.run(debug=False)
