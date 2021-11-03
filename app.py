# Importation des modules externes (ce sont des modules codées par d'autre dev, un module est un genre de plugin).
from flask import Flask, render_template, redirect
from pathlib import Path

# Importation des modules internes, ce sont les modules que nous avons créé pour ce projet.
from articles import *


app = Flask(__name__) # Ligne obligatoire qui défini que ce fichier est une app Flask (c'est le framework que l'on utilise pour faire notre backend)

article_data=[first_week, second_week,third_week,fourth_week,fifth_week] # On crée une liste contenant toute nos semaine


@app.route("/") # Route de l'application si il n'y a rien après l'URL.
def void_redirect():
    """Redirects the user to a different route

    Returns:
        [redirect]: Change current user's page 
    """
    return redirect("/accueil") # On redirige l'utilisateur vers la page d'accueil

@app.route("/accueil") # Route de la page d'accueil
def home_page():
    pass

@app.route("/nos-articles") # Route de l'index de nos articles
def article_theme_lister():
    """Renders a theme list

    Returns:
        [html]: rendered page from the indicated template
    """
    return render_template("article_lister.html", article_data=article_data ) # On crée une page ou on affiche toute les semaines

@app.route("/nos-articles/<theme>") # Route dynamique pour les différents themes dans nos-articles
def article_theme_index(theme):
    """Renders a theme page with its articles.

    Args:
        theme (str): The theme our user is on

    Returns:
        [html]: rendered page from the indicated template
    """
    for item in article_data: # Itération dans chaque semaine
        if theme in item["name"]: # Si le nom de la semaine correspond a un nom de semaine dans toute nos semaines =>
            return render_template("article_theme_index.html", article_data=item, current_page=theme) # On crée la page article_theme_index qui contient tout les articles du theme actuel
    return render_template("404.html") # Si le theme est pas dans une des semaines on renvoie l'utilisateur sur une 404.

@app.route("/nos-articles/<theme>/<current_article>") # Route dynamique pour les différents articles dans chaque theme de nos articles
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
