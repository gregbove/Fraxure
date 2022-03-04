# https://towardsdatascience.com/build-deploy-a-react-flask-app-47a89a5d17d9

from flask import Flask, send_from_directory

# app = Flask(__name__, static_url_path="", static_folder="frontend/build")
app = Flask(__name__, static_url_path="", static_folder="frontend/build")


@app.route("/", defaults={"path": ""})
def serve(path):
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run()
