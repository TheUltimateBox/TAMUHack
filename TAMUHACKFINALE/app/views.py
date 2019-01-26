
from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/account')
def account():
    return render_template("about.html")

@app.route('/aboutfooder')
def about():
    return render_template("aboutfooder.html")