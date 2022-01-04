from app import data_base
from datetime import datetime
import re
from flask_security import UserMixin, RoleMixin


# функция слагификации
def slugify(s):
    # r сообщает интерпретатору считывать знаки и символы "как есть"
    pattern = r'[^\w+]'
    # ищет по шаблону pattern меняет на "-" в переменной s
    return re.sub(pattern, '-', s)

# Модель запросов в б.д.
class Records(data_base.Model):
    # столбцы базы
    id = data_base.Column(data_base.Integer, primary_key=True)
    company_name = data_base.Column(data_base.String(100), unique=True)
    # человекопонятные ссылки
    slug = data_base.Column(data_base.String(100), unique=True)
    # краткий отчёт
    short_info = data_base.Column(data_base.Text)
    # полный отчёт(ссылка)
    long_info = data_base.Column(data_base.String(300))
    # дата и время добавления в б.д.
    updated = data_base.Column(data_base.DateTime, default=datetime.now())

    # *args список позиционных аргументов, **kwargs словарь именованных аргументов
    def __init__(self, *args, **kwargs):
        # вызываем конструктор клааса предка Model у класса Records
        # __init__ передаёт в конструктор класса Model аргументы с входа __init__ конструктора Records
        super(Records, self).__init__(*args, **kwargs)
        self.generate_slug()

    # создаём генератор человеко понятных ссылок
    def generate_slug(self):
        if self.company_name:
            self.slug = slugify(self.company_name)

    def __repr__(self):
        return f'<Record id: {self.id}, title: {self.company_name}>'



# Пользователи и модели ролей

# связи таблиц
roles_users = data_base.Table('roles_users',
        data_base.Column('user_id', data_base.Integer(), data_base.ForeignKey('user.id')),
        data_base.Column('role_id', data_base.Integer(), data_base.ForeignKey('role.id'))
    )

class User(data_base.Model, UserMixin):
    id = data_base.Column(data_base.Integer(), primary_key=True)
    full_name = data_base.Column(data_base.String(255))
    gender = data_base.Column(data_base.String(100))
    email = data_base.Column(data_base.String(100), unique=True)
    password = data_base.Column(data_base.String(255))
    active = data_base.Column(data_base.Boolean())
    # св-во таблицы
    roles = data_base.relationship('Role', secondary=roles_users, backref=data_base.backref('users', lazy='dynamic'))

class Role(data_base.Model, RoleMixin):
    id = data_base.Column(data_base.Integer(), primary_key=True)
    name = data_base.Column(data_base.String(100), unique=True)
    description = data_base.Column(data_base.String(255))

# отбражение роли в админке
    def __repr__(self):
        return self.name