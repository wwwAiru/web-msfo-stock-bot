from flask import Blueprint, render_template, request, redirect, url_for, flash
from user_profile.registration_form import ExtendedRegisterForm
from user_profile.create_test_user_form import TestUserForm
from app import data_base
from flask_security import login_required, current_user, roles_accepted
from datetime import datetime, timedelta
from models import User
from os import urandom
from flask_security.cli import hash_password



# блюпринт кусок изолированной функциональности
# record обработчик блюпринта
# аргументы: название блюпринта, приложение, и путь к шаблонам
user_profile = Blueprint('user_profile', __name__, template_folder='templates')



# страница представления профиля пользователя
@user_profile.route('/', methods=['POST', 'GET'])
@login_required
def index():
    return render_template('user_profile/index.html')


# роут для формы редактирования профиля
@user_profile.route('/edit/', methods=['POST', 'GET'])
@login_required
def edit_profile():
    # получаем данные из объекта пользователя current_user
    if request.method == 'POST':
        form = ExtendedRegisterForm(formdata=request.form, obj=current_user)
        # метод populate_obj заменяет данными поля формы
        form.populate_obj(current_user)
        # комит для б.д. чтобы сохранить изменения
        data_base.session.commit()
        return redirect(url_for('user_profile.index'))
    form = ExtendedRegisterForm(obj=current_user)
    return render_template('user_profile/edit_profile.html', form=form)


# роут для создания тестового пользователя админом
@user_profile.route('/create_test_user', methods=['POST', 'GET'])
@login_required
@roles_accepted('admin')
def create_test_user():
    test_user_form = TestUserForm()
    if test_user_form.validate_on_submit() and current_user.has_role('admin'):
        email = test_user_form.email.data
        password = test_user_form.password.data
        last_name = test_user_form.last_name.data
        first_name = test_user_form.first_name.data
        middle_name = test_user_form.middle_name.data
        gender = test_user_form.gender.data
        birthdate = test_user_form.birthdate.data
        confirmed_at = datetime.utcnow() + timedelta(hours=3)
        try:
            user = User(email=email,
                        password=hash_password(password),
                        last_name=last_name,
                        first_name=first_name,
                        middle_name=middle_name,
                        gender=gender,
                        birthdate=birthdate,
                        confirmed_at=confirmed_at,
                        active=True,
                        fs_uniquifier=urandom(16).hex())
            data_base.session.add(user)
            data_base.session.commit()
            flash(message='Пользователь успешно создан', category='success')
        except:
            data_base.session.rollback()
            flash(message='Пользователь уже существует', category='danger')
        return redirect(url_for('user_profile.create_test_user'))
    return render_template('user_profile/create_test_user.html', test_user_form=test_user_form)
