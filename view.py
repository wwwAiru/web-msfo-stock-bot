from app import app, data_base
from flask import render_template, redirect, url_for, flash
from models import AboutProject




@app.route('/')
def index():
    about = AboutProject.query.first()
    return render_template('index.html', about=about)
