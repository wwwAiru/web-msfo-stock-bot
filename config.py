
class Configuration(object):
    DEBUG = True
    #Если установлен в True, то Flask-SQLAlchemy будет отслеживать изменения объектов и посылать сигналы.
    #Отключим чтобы не влиял на производительность
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://ujkbzy:jVr8gf3BkBDb2k2I@localhost/bot_db'
    # без ключа некоторый функционал может быть недоступен, например объект сессии(куки серв-клиент)
    SECRET_KEY = 'Hdf72Lkfj872ZWq83Lru32imn'
    # flask-security соль и хэш для паролей
    SECURITY_PASSWORD_SALT = 'f3BkBDa8k4Wz9h'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
