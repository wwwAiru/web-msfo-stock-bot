from wtforms import StringField, EmailField, SelectField, PasswordField, DateField
from flask_wtf import FlaskForm
from wtforms.validators import Email, InputRequired, EqualTo, length, Regexp


class Reg_form(FlaskForm):
    first_name = StringField('Имя: ', validators=[InputRequired(), length(max=20)])
    last_name = StringField('Фамилия: ', validators=[InputRequired(), length(max=20)])
    middle_name = StringField('Отчество: ', validators=[InputRequired(), length(max=20)])
    email = EmailField('Почта: ', validators=[InputRequired(), Email(), length(max=100)])

    password = PasswordField('Пароль: ', validators=[InputRequired(),
                        EqualTo('confirm_pass', message='Пароли не совпадают. '),
                        length(min=8, max=255, message='Пароль должен быть не менее 8 символов. '),
                        Regexp('(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%\-*#?&;:"\'])[A-Za-z\d@$!%\-*#?&;:"\']', message=
                        'Пароль должен содержать минимум один символ в нижнем регистре, один в верхнем регистре, цифру, спецсимвол например: @$!%\-*#?&;:"\' ' )])

    confirm_pass = PasswordField('Повторите пароль: ', validators=[InputRequired()])

    gender = SelectField('Пол: ', choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')])
    birthdate = DateField('Дата рождения', validators=[InputRequired()])
