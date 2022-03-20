from datetime import datetime
import os

# временная мера
with open('pww91.wim', 'r', encoding="utf-8") as f:
    passw = f.read()

class Configuration(object):

    # режим отладки приложения позволяет применять изменения в коде без перезагрузки
    DEBUG = True
    # Если SQLALCHEMY_TRACK_MODIFICATIONS установлен в True, то Flask-SQLAlchemy будет отслеживать изменения объектов и
    # посылать алерты. Отключил чтобы не влиял на производительность.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.db3'
    # таймаут подключения б.д.
   # SQLALCHEMY_POOL_RECYCLE = 60
   # SQLALCHEMY_POOL_SIZE = 20
    # без ключа некоторый функционал может быть недоступен, например объект сессии(куки серв-клиент)
    SECRET_KEY = 'Hdf72Lkfj872ZWq83Lru32imn'
    # Выключил ASCII чтобы jsonfy мог передавать UTF-8 символы
    JSON_AS_ASCII = False
    # flask-security соль и хэш для паролей
    SECURITY_PASSWORD_SALT = 'f3BkBDa8k4Wz9h'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    # настройки регистрации flask_security
    SECURITY_DATETIME_FACTORY = datetime.utcnow
    SECURITY_REGISTERABLE = True
    # необходимость авторизации после подтверждения
    SECURITY_AUTO_LOGIN_AFTER_CONFIRM = False
    SECURITY_REGISTER_URL = '/registration'
    SECURITY_CONFIRMABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TOKEN_MAX_AGE = 60*60*24*3
    # настройки почтового сервера
    MAIL_SERVER = 'smtp.mail.ru'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'msfostockbot@mail.ru'
    MAIL_PASSWORD = passw
    MAIL_DEFAULT_SENDER = 'msfostockbot@mail.ru'

    # тема для письма подтверждения
    SECURITY_EMAIL_SUBJECT_CONFIRM = 'Техническое письмо'
    # перенаправление после подтверждения
    SECURITY_POST_REGISTER_VIEW = 'security.login'
    SECURITY_POST_CONFIRM_VIEW = 'security.login'
    # перенаправление после смены пароля
    SECURITY_POST_CHANGE_VIEW = 'security.change_password'
    # тема для письма
    SECURITY_EMAIL_SUBJECT_REGISTER = 'Добро пожаловать!'


