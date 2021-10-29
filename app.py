from _typeshed import ReadOnlyBuffer
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("test.html",  idiot="clément est PD")