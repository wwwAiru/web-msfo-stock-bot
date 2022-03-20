from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SelectField, DateField, PasswordField
from wtforms.validators import InputRequired, EqualTo, Length, Email


class TestUserForm(FlaskForm):
    email = EmailField('Электронная почта: ', validators=[InputRequired(), Email()])
    password = PasswordField('Пароль: ', validators=[InputRequired('введите пароль'),
                                                     EqualTo('password_confirm', message='Пароли не совпадают. '),
                                                     Length(min=4, max=255, message='Пароль должен быть не менее 4 символов.')
                                                     ])
    password_confirm = PasswordField('Повторите пароль: ', validators=[InputRequired('повторите пароль')])
    last_name = StringField('Фамилия: ', validators=[InputRequired('введите фамилию'), Length(max=50)])
    first_name = StringField('Имя: ', validators=[InputRequired('введите имя'), Length(max=50)])
    middle_name = StringField('Отчество: ', validators=[InputRequired('введите отчество'), Length(max=50)])
    gender = SelectField('Пол: ', choices=[('Мужской', 'Мужской'), ('Женский', 'Женский')])
    birthdate = DateField('Дата рождения', validators=[InputRequired('введите дату рождения')])
