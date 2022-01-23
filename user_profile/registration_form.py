from wtforms import StringField, SelectField, PasswordField, DateField
from wtforms.validators import InputRequired, EqualTo, length, Regexp
from flask_security.forms import ConfirmRegisterForm



# Расширил класс ConfirmRegisterForm и переопределил валидацию пароля по современным стандартам
class ExtendedRegisterForm(ConfirmRegisterForm):
    password = PasswordField('Пароль: ', validators=[InputRequired(),
                                                     EqualTo('password_confirm', message='Пароли не совпадают. '),
                                                     length(min=8, max=255,
                                                            message='Пароль должен быть не менее 8 символов. '),
                                                     Regexp(
                                                         '(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_@$!%\-*#?&;:"\'])[A-Za-z\d_@$!%\-*#?&;:"\']',
                                                         message=
                                                         'Пароль должен содержать минимум один символ в нижнем регистре, '
                                                         'один в верхнем регистре, цифру, спецсимвол например: _@$!%\-*#?&;:"\' ')])

    password_confirm = PasswordField('Повторите пароль: ', validators=[InputRequired()])
    last_name = StringField('Фамилия: ', validators=[InputRequired(), length(max=50)])
    first_name = StringField('Имя: ', validators=[InputRequired(), length(max=50)])
    middle_name = StringField('Отчество: ', validators=[InputRequired(), length(max=50)])
    gender = SelectField('Пол: ', choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')])
    birthdate = DateField('Дата рождения', validators=[InputRequired()])



