from flask import Flask, redirect, url_for, request
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
# для миграций б.д.
from flask_migrate import Migrate
# адмминка
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security, current_user
from flask_babelex import Babel


app = Flask(__name__)
app.config.from_object(Configuration)
data_base = SQLAlchemy(app)
babel = Babel(app)
# создал объект класса Migrate в качестве параметров app и data_base для их корреяции
migrate = Migrate(app, data_base)

# Админка
from models import *

# Для того чтобы ограничить отображение админки созд. два класса от родительских ModelView и AdminIndexView
# класс AdminView ограничивает вывод функционала админки
class AdminView(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        # параметр next перенаправляет на страницу куда мы хотели направиться будучи неавторизованным
        return redirect( url_for('security.login', next=request.url) )

# класс AdminPanel не даёт видеть админ панель будучи неавторизованным
class AdminPanel(AdminIndexView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect( url_for('security.login', next=request.url) )



# создан экземпляр класса Admin
admin = Admin(app, '@Msfo_stock_bot' , template_mode='bootstrap4', url='/', index_view=AdminPanel(name='Панель администратора'))
# ModelView или расширеный от него, в нашем случае, AdminView - подхватывает классы б.д. из models.py
# и реализуем модель 'C.R.U.D.' для управлением любыми данными из б.д.
# параметром name можно назначить название кнопок на панели администратора.
admin.add_view(AdminView(Records, data_base.session, name='Таблица МСФО/РСБУ'))
admin.add_view(AdminView(User, data_base.session, name='Таблица пользователей'))
admin.add_view(AdminView(Role, data_base.session, name='Роли'))


# локализация админки
@babel.localeselector
def get_locale():
    # Put your logic here. Application can store locale in
    # user profile, cookie, session, etc.
    return 'ru'

# flask_security
# созд. экземпляр класса SQLAlchemyUserDatastore, аргументы: б.д., классы User и Role из models.py
user_datastore = SQLAlchemyUserDatastore(data_base, User, Role)
# созд. экземпляр класса Security с аргументами: приложение, объект user_datastore
security = Security(app, user_datastore)