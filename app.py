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
        redirect: Change current user's page 
    """
    return redirect("/a-la-une") # On redirige l'utilisateur vers la page d'accueil

@app.route("/a-la-une") # Route de la page d'accueil
def home_page():
    return render_template("home.html", week_list=article_data)

@app.route("/nos-articles") # Route de l'index de nos articles
def article_theme_lister():
    """Renders a theme list

    Returns:
        html: rendered page from the indicated template
    """
    return render_template("article_lister.html", article_data=article_data ) # On crée une page ou on affiche toute les semaines

@app.route("/nos-articles/<theme>") # Route dynamique pour les différents themes dans nos-articles
def article_theme_index(theme):
    """Renders a theme page with its articles.

    Args:
        theme (str): The theme our user is on

    Returns:
        html: rendered page from the indicated template
    """

    # Ici theme est égal a ce qui est dans l'url apres "nos-articles/"

    verification = page_verificator(theme) # On teste si la page actuelle correspond a un nom de semaine, il est important de stocker ça dans une variable car on aura besoin des données de la semaine que la fonction page_verificator nous renvoie
    if verification[0] == True: # Si page_verificator a renvoyé un True dans la premiere valeur du tuple
        return render_template("article_theme_index.html", article_data=verification[1], current_page=theme) # On crée la page article_theme_index qui contient tout les articles de la semaine actuelle
    return render_template("404.html") # Si le theme n'est pas dans une des semaines on renvoie l'utilisateur sur une 404.

@app.route("/nos-articles/<theme>/<current_article>") # Route dynamique pour les différents articles dans chaque theme de nos articles
def article_build(theme, current_article):
    """Renders current_article page

    Args:
        theme (str): The theme our user is on
        current_article (str): The article our user is on

    Returns:
        html: rendered page of the current article
    """

    # Ici current_article est égal a ce qui est dans l'url apres "nos-articles/{theme}/"

    verification = page_verificator(theme) # On teste si la page actuelle correspond a un nom de semaine, il est important de stocker ça dans une variable car on aura besoin des données de la semaine que la fonction page_verificator nous renvoie
    for article in verification[1]["article"]: # on itère chaque article de la semaine
        if current_article in article["title"]: # si le nom de l'article est dans les articles de la semaine
            return render_template("article_builder.html", current_article=article) # On crée la page avec les données de l'article actuel
    return render_template("404.html") # Si current_article n'est pas dans un article on renvoie l'utilisateur sur une 404.


def page_verificator(current_page:str) -> tuple:
    """Verify if a str is in article_date

    Args:
        current_page (str): string to test

    Returns:
        tuple: False or true tuple containing week's data if true
    """
    for week in article_data: # Itération dans chaque semaine
        if current_page == week["name"]: # Si le nom de la semaine correspond a un nom de semaine dans toute nos semaines =>
            return (True, week) # On retourne un tuple qui contient True et les données de la page actuelle
    return (False, None)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404