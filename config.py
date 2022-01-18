
class Configuration(object):

    # режим отладки приложения позволяет применять изменения в коде без перезагрузки
    DEBUG = True

    # Если SQLALCHEMY_TRACK_MODIFICATIONS установлен в True, то Flask-SQLAlchemy будет отслеживать изменения объектов и
    # посылать алерты. Отключил чтобы не влиял на производительность.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://ujkbzy:jVr8gf3BkBDb2k2I@localhost/bot_db'

    # без ключа некоторый функционал может быть недоступен, например объект сессии(куки серв-клиент)
    SECRET_KEY = 'Hdf72Lkfj872ZWq83Lru32imn'

    # flask-security соль и хэш для паролей
    SECURITY_PASSWORD_SALT = 'f3BkBDa8k4Wz9h'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    # настройки регистрации flask_security
    SECURITY_REGISTERABLE = True
    SECURITY_REGISTER_URL = '/registration'
    SECURITY_CONFIRMABLE = True
    SECURITY_RECOVERABLE = True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = '*'
    MAIL_PASSWORD = '*'
    MAIL_DEFAULT_SENDER = '*'

