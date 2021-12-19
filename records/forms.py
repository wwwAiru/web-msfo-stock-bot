from wtforms import Form, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class Record_form(Form):
    company_name = StringField('Название компании: ', validators=[DataRequired()])
    short_info = TextAreaField('Краткий отчёт: ')
    long_info = StringField('Ссылка на полный отчёт: ', validators=[DataRequired()])