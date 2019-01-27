
from flask import render_template

from app import app

@app.route('/prelogin')
def login():
    return render_template("login.html")

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/afterLogin')
def loggedIn():
    return render_template("loggedIn.html")


@app.route('/preferences')
def preferences():
    return render_template("preferences.html")


@app.route('/swipe')
def swipe():
    return render_template("swipe.html")


@app.route('/signIn')
def signIn():
    return render_template("index.html")

# @app.route('/aboutfooder')
# def about():
#     return render_template("aboutfooder.html")