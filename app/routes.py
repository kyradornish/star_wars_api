from app import app
from flask import render_template, url_for, redirect, flash, request, session
from app.forms import SearchForm, getCharacterInfo, searchCharacterInfo, getListCharacters, sortCharacters, planetResidents


@app.route("/", methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        name = form.name.data
        return redirect (url_for('character', name=name))
    return render_template("index.html", form=form, title="Home")

@app.route("/character/<name>", methods=['GET'])
def character(name):
    results = searchCharacterInfo(name)
    return render_template("character.html", results=results, title=name)

@app.route("/character/luke", methods=['GET'])
def luke():
    results = getCharacterInfo("1")
    return render_template("character.html", results=results, title="Luke")

@app.route("/character/leia", methods=['GET'])
def leia():
    results = getCharacterInfo("5")
    return render_template("character.html", results=results, title="Leia")

@app.route("/character/han", methods=['GET'])
def han():
    results = getCharacterInfo("14")
    return render_template("character.html", results=results, title="Han")

@app.route("/characters", methods=['GET'])
def characters():
    results = getListCharacters()
    return render_template("characters.html", results=results, title="List of Characters")

@app.route("/characters/sort/<by>", methods=['GET'])
def sort(by):
    results = sortCharacters(by)
    return render_template("characters.html", results=results, title="Characters Sorted")

@app.route("/planet-residents", methods=['GET'])
def residents():
    results = planetResidents()
    return render_template("planet-residents.html", results=results, title="Planet Residents")
