from app import app, data_base
from flask import render_template, request, redirect, url_for, flash
from registration_form import Reg_form
from models import User




@app.route('/')
def index():
    return render_template('index.html')



@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        middle_name = request.form['middle_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        birthdate = request.form['birthdate']
        full_name = f'{last_name} {first_name} {middle_name}'
        try:
            user = User(full_name=full_name, email=email, password=password, gender=gender, birthdate=birthdate)
            data_base.session.add(user)
            data_base.session.commit()
            return redirect(url_for('security.login'))
        except:
            data_base.session.rollback()
            flash('Адрес электронной почты уже используется')
            print('Ошибка записи в базу данных.')
    forms = Reg_form()
    return render_template('registration.html', forms=forms)