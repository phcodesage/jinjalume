from flask import Flask, render_template

from jinjalume import Jinjalume

app = Flask(__name__)
Jinjalume(app)


@app.get("/")
def index():
    return render_template("index.html")
