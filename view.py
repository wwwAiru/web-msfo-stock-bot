from app import app, data_base
from flask import render_template, redirect, url_for, flash
from models import AboutProject




@app.route('/')
def index():
    about = AboutProject.query.first_or_404()
    return render_template('index.html', about=about)

# страница 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
