from typing import Match
from flask import Flask, render_template
import json
from pathlib import Path
import os

from articles import *


working_dir = Path.cwd()

app = Flask(__name__)

article_data=[first_week, second_week,third_week,fourth_week,fifth_week]

@app.route("/nos-articles")
def article_theme_lister():
    return render_template("article_lister.html", article_data=article_data )

@app.route("/nos-articles/<theme>")
def article_theme_index(theme):
    for item in article_data:
        if theme in item["name"]:
            return render_template("article_theme_index.html", article_data=item, current_page=theme)
    return render_template("article_theme_index.html", article_data=article_data, current_page=theme)
    
