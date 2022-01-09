from wtforms import Form, StringField, EmailField, SelectField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired, length


class Reg_form(Form):
    first_name = StringField('Имя: ', validators=[DataRequired(), length(max=20)])
    last_name = StringField('Фамилия: ', validators=[DataRequired(), length(max=20)])
    middle_name = StringField('Отчество: ', validators=[DataRequired(), length(max=20)])
    email = EmailField('Почта: ', validators=[InputRequired('Введите адрес электронной почты.'),
                Email('В этом поле нужно указать действующий адрес электронной почты'), length(max=100)])
    password = PasswordField('Пароль: ', validators=[DataRequired(), length(max=255)])
    gender = SelectField('Пол: ', choices=[('male', 'Мужской'), ('female', 'Женский')])
    birthdate = DateField('Дата рождения')

