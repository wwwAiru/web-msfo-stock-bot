from flask import Blueprint, render_template, request, redirect, url_for
from user_profile.registration_form import ExtendedRegisterForm
from app import data_base
from flask_security import login_required, current_user



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
