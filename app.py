from typing import Match
from flask import Flask, render_template, redirect
import json
from pathlib import Path
import os

from articles import *


working_dir = Path.cwd()

app = Flask(__name__)

article_data=[first_week, second_week,third_week,fourth_week,fifth_week]


@app.route("/")
def void_redirect():
    return redirect("/accueil")

@app.route("/accueil")
def home_page():
    pass

@app.route("/nos-articles")
def article_theme_lister():
    return render_template("article_lister.html", article_data=article_data )

@app.route("/nos-articles/<theme>")
def article_theme_index(theme):
    for item in article_data:
        if theme in item["name"]:
            return render_template("article_theme_index.html", article_data=item, current_page=theme)
    return render_template("404.html")

@app.route("/nos-articles/<theme>/<current_article>")
def article_build(theme, current_article):
    for item in article_data:
        if theme in item["name"]:
            print("Current theme is " + theme )
            for article in item["article"]:
                print("Testing :" + str(article))
                if current_article in article["title"]:
                    print("Clicked article is " + str(article))
                    current_article_data = article
                    return render_template("article_builder.html", current_article=current_article_data)
    return render_template("404.html")
