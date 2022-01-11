from app import app, data_base
from flask import render_template, redirect, url_for, flash
from registration_form import Reg_form
from models import User
from app import user_datastore
from flask_security.cli import hash_password



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = Reg_form()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        middle_name = form.middle_name.data
        email = form.email.data
        password = hash_password(form.password.data)
        gender = form.gender.data
        birthdate = form.birthdate.data
        full_name = f'{last_name} {first_name} {middle_name}'

        if not user_datastore.find_user(email=email):
            try:
                user = User(full_name=full_name, email=email, password=password, gender=gender, birthdate=birthdate)
                data_base.session.add(user)
                data_base.session.commit()
                flash(f'{first_name} {middle_name}, Вы успешно зарегестрированы!', "success")
                return redirect(url_for('security.login'))
            except:
                data_base.session.rollback()
                print('Ошибка записи в базу данных.')
        else:
            flash(f'Адрес электронной почты {email} уже используется')
    else:
        pass
    return render_template('registration.html', form=form)