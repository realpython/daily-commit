from project import app


@app.route("/ping")
def index():
    return "pong!"
