from flask import Blueprint
from flask import render_template
from models import Records



# блюпринт кусок изолированной функциональности
# record обработчик блюпринта
records = Blueprint('records', __name__, template_folder='templates') #аргументы: название блюпринта, приложение, и путь к шаблонам


# страница представления таблицы
@records.route('/')
def index():
    records = Records.query.all()
    return render_template('records/index.html', records=records)

# поиск по слагу в б.д. <...> - это переменная динамической ссылки
@records.route('/<slug>')
def record_detail(slug):
    # query.filter может выдать запрос списком если нашлось несколько результатов,
    # так как слаг уникальный, то берём первый попавшийся результат ( метод .first() )
    record = Records.query.filter(Records.slug == slug).first()
    print(record)
    # возвращается страница с детальной информацией о компании
    return render_template('records/record_detail.html', record=record)