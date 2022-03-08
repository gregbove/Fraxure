# https://towardsdatascience.com/build-deploy-a-react-flask-app-47a89a5d17d9

from flask import Flask, send_from_directory, render_template

app = Flask(
    "Fraxure", static_url_path="/page", static_folder="../frontend/build/static"
)


@app.route("/")
def serve_static_react():
    return send_from_directory("index.html")


# @app.route("/")
# def index():
#     return "Index Page"


@app.route("/api/")
def api_route():
    return "this accesses the api"


if __name__ == "__main__":
    app.run(debug=True)
