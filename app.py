from flask import Flask, redirect, url_for, request
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
# для миграций б.д.
from flask_migrate import Migrate
# админка
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from user_profile.registration_form import ExtendedRegisterForm
from user_profile.reset_change_forms import ExtendedResetForm, ExtendedChangeForm
from flask_security import SQLAlchemyUserDatastore, Security, current_user
from flask_babelex import Babel
from flask_mail import Mail
# импорт полей форм для замены полей на простенький текстовый редактор
from wtforms import TextAreaField
from wtforms.widgets import TextArea



app = Flask(__name__)
app.config.from_object(Configuration)
data_base = SQLAlchemy(app)
babel = Babel(app)
mail = Mail(app)
# создал объект класса Migrate в качестве параметров app и data_base для их корреяции
migrate = Migrate(app, data_base)


# импорт моделей для админки
from models import *


# Для того чтобы ограничить отображение админки созд. два класса от родительских ModelView и AdminIndexView
# класс AdminView ограничивает вывод функционала админки без доступа
class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')


    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


# дополнение класса ModelView чтобы slug генерировался в админке автоматически при создании новой записи в таблице
class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class ApiModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_key()
        return super(ApiModelView, self).on_model_change(form, model, is_created)

class ApiAdminView(AdminMixin ,ApiModelView):
    column_display_pk = True
    form_columns = ['id', 'description']


# класс AdminView ограничивает модели представления б.д. в админке
class AdminView(AdminMixin, ModelView):
    pass


# класс AdminPanel ограничивает админ панель будучи неавторизованным
class AdminPanelView(AdminMixin, AdminIndexView):
    @expose('/')
    def admin_index_view(self):
        adm_info = AdminInformation.query.first_or_404()
        return self.render('admin/index.html', adm_info=adm_info)


# создал ещё наследников вьюх RecordsAdminView, UserAdminView, RoleAdminView
# чтобы метод generate_slug не попал в те модели, где его нет изначально
class RecordsAdminView(AdminMixin, BaseModelView):
    # так можно переопределить отображение форм в админ панели
    form_columns = ['company_name', 'short_info', 'long_info']
    column_searchable_list = ['company_name', 'short_info']
    page_size = 5

class UserAdminView(AdminMixin, ModelView):
    column_searchable_list = ['email', 'first_name', 'last_name', 'middle_name']
    page_size = 10

class RoleAdminView(AdminMixin, ModelView):
    pass

# изменение полей flask-wtf на CKeditor
class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)

class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()

# CKeditor в админке('о проекте')
class AboutAdminView(AdminMixin, ModelView):
    """extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

    form_overrides = {
        'body': CKTextAreaField,
        'title': CKTextAreaField,
        'contact_us': CKTextAreaField
    }"""
    pass

# создан экземпляр класса Admin
admin = Admin(app, '@Msfo_stock_bot', template_mode='bootstrap4', url='/',
              index_view=AdminPanelView(name='Инструкция'))
# ModelView или расширеный от него, в нашем случае, AdminView - подхватывает классы б.д. из models.py
# и реализуем модель 'C.R.U.D.' для управлением любыми данными из б.д.
# параметром name можно назначить название кнопок на панели администратора.
admin.add_view(RecordsAdminView(Records, data_base.session, name='Таблица МСФО/РСБУ'))
admin.add_view(UserAdminView(User, data_base.session, name='Пользователи'))
admin.add_view(RoleAdminView(Role, data_base.session, name='Роли'))
admin.add_view(ApiAdminView(ApiKey, data_base.session, name='API ключи'))
admin.add_view(AboutAdminView(AboutProject, data_base.session, name='О проекте'))
admin.add_view(AdminView(AdminInformation, data_base.session, name='Инструкция ред.'))




# локализация flask-security
@babel.localeselector
def get_locale():
    return 'ru'



# flask_security
# созд. экземпляр класса SQLAlchemyUserDatastore, аргументы: б.д., классы User и Role из models.py
user_datastore = SQLAlchemyUserDatastore(data_base, User, Role)
# созд. экземпляр класса Security с аргументами: приложение, объект user_datastore, кастомный класс с формой регистрации
security = Security(app, user_datastore, confirm_register_form=ExtendedRegisterForm,
                                         reset_password_form=ExtendedResetForm,
                                         change_password_form=ExtendedChangeForm,
                                         register_form=ExtendedRegisterForm)

