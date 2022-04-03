from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class Record_form(FlaskForm):
    company_name = StringField('Название компании: ', validators=[DataRequired()])
    short_info = TextAreaField('Краткий отчёт: ')
    long_info = StringField('Ссылка на полный отчёт: ', validators=[DataRequired()])
    