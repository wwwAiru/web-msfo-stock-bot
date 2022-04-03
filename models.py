from app import data_base
from datetime import datetime, timedelta
from flask_security import UserMixin, RoleMixin
# библиотека для транслита слагификации
from pytils.translit import slugify
from os import urandom


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
    updated = data_base.Column(data_base.DateTime, default=datetime.utcnow()+timedelta(hours=3))

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
    email = data_base.Column(data_base.String(100), unique=True)
    password = data_base.Column(data_base.String(255))
    last_name = data_base.Column(data_base.String(50))
    first_name = data_base.Column(data_base.String(50))
    middle_name = data_base.Column(data_base.String(50))
    gender = data_base.Column(data_base.String(100))
    birthdate = data_base.Column(data_base.Date())
    updated = data_base.Column(data_base.DateTime, default=datetime.utcnow()+timedelta(hours=3))
    confirmed_at = data_base.Column(data_base.DateTime())
    active = data_base.Column(data_base.Boolean())
    fs_uniquifier = data_base.Column(data_base.String(64), unique=True)
    # св-во таблицы
    roles = data_base.relationship('Role', secondary=roles_users, backref=data_base.backref('users', lazy='dynamic'))

    # отбражение юзера в ролях админки
    def __repr__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}  ({self.email})'


class Role(data_base.Model, RoleMixin):
    id = data_base.Column(data_base.Integer(), primary_key=True)
    name = data_base.Column(data_base.String(100), unique=True)
    description = data_base.Column(data_base.String(255))

    # отбражение роли в админке
    def __repr__(self):
        return self.name

# модель страницы "О проекте"
class AboutProject(data_base.Model):
    id = data_base.Column(data_base.Integer(), primary_key=True)
    title = data_base.Column(data_base.String(255))
    body = data_base.Column(data_base.Text)
    updated = data_base.Column(data_base.DateTime, default=datetime.utcnow()+timedelta(hours=3))
    contact_us = data_base.Column(data_base.Text)

class AdminInformation(data_base.Model):
    id = data_base.Column(data_base.Integer(), primary_key=True)
    title = data_base.Column(data_base.String(255))
    body = data_base.Column(data_base.Text)
    updated = data_base.Column(data_base.DateTime, default=datetime.utcnow()+timedelta(hours=3))

# модель генерации API ключей
class ApiKey(data_base.Model):
    id = data_base.Column(data_base.Integer(), primary_key=True)
    key = data_base.Column(data_base.String(100), unique=True)
    description = data_base.Column(data_base.Text)

    def __init__(self, *args, **kwargs):
        # вызываем конструктор клааса предка Model у класса Records
        # __init__ передаёт в конструктор класса Model аргументы с входа __init__ конструктора Records
        super(ApiKey, self).__init__(*args, **kwargs)
        self.generate_key()

    def generate_key(self):
        self.key = urandom(30).hex()

    def __repr__(self):
        return self.key
