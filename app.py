from flask import Flask, render_template
import json
from pathlib import Path
import os

from articles import *


working_dir = Path.cwd()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("test.html",  idiot="clément est PD")

@app.route("/nos-articles")
def article_theme_lister():
    article_data=[first_week, second_week,third_week,fourth_week,fifth_week]
    
    print(article_data)

    return render_template("article_lister.html", article_data=article_data )

@app.route("/articles")
def articles_title_lister():
    
    return render_template("article_lister.html",  json_data=first_week)




