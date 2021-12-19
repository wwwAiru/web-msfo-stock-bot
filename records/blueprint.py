from flask import Blueprint
from flask import render_template
from models import Records
from flask import request
from .forms import Record_form


# блюпринт кусок изолированной функциональности
# record обработчик блюпринта
# аргументы: название блюпринта, приложение, и путь к шаблонам
records = Blueprint('records', __name__, template_folder='templates')


@records.route('/create_record', methods = ['POST', 'GET'])
def create_record():
    form = Record_form()
    return render_template('records/create_record.html', form=form)



# страница представления таблицы
@records.route('/', methods = ['POST', 'GET'])
def index():
    # в переменную search считывается то, что пользователь ввёл в строку поиска
    # далее условие: если переменная search содержит что - либо, тогда у класса Records - модели запросов в б.д.
    # запрашиваем данные по сравниванию пользовательского запроса с именами компаний или содержанию краткого отчёта
    search = request.args.get('search')
    if search:
        records = Records.query.filter(Records.company_name.contains(search) | Records.short_info.contains(search)).all()
    # иначе рендерится страница со всеми записями
    else:
        records = Records.query.all()
    return render_template('records/index.html', records=records)

# поиск по слагу в б.д. <...> - это переменная динамической ссылки
@records.route('/<slug>')
def record_detail(slug):
    # query.filter может выдать запрос списком если нашлось несколько результатов,
    # так как слаг уникальный, то берём первый попавшийся результат ( метод .first() )
    record = Records.query.filter(Records.slug == slug).first()
    # возвращается страница с детальной информацией о компании
    return render_template('records/record_detail.html', record=record)