from flask import Blueprint, render_template, request, redirect, url_for
from models import Records
from .forms import Record_form
from app import data_base


# блюпринт кусок изолированной функциональности
# record обработчик блюпринта
# аргументы: название блюпринта, приложение, и путь к шаблонам
records = Blueprint('records', __name__, template_folder='templates')


@records.route('/create_record', methods = ['POST', 'GET'])
def create_record():
    if request.method == 'POST':
        company_name = request.form['company_name']
        short_info = request.form['short_info']
        long_info = request.form['long_info']
        try:
            record = Records(company_name=company_name, short_info=short_info, long_info=long_info)
            data_base.session.add(record)
            data_base.session.commit()
        except:
            print('Ошибка записи в базу данных.')
        return redirect( url_for('records.index') )
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
        records = Records.query.order_by(Records.updated.desc()).all()
        # тут небольшое форматирование вывода даты, мне удобно в формате: день.месяц.год
        # можно настроить в любом удобном формате
        for record in records:
            record.updated=record.updated.strftime("%d.%m.%Y %H:%M:%S")
    return render_template('records/index.html', records=records)

# поиск по слагу в б.д. <...> - это переменная динамической ссылки
@records.route('/<slug>')
def record_detail(slug):
    # query.filter может выдать запрос списком если нашлось несколько результатов,
    # так как слаг уникальный, то берём первый попавшийся результат ( метод .first() )
    record = Records.query.filter(Records.slug == slug).first()
    # возвращается страница с детальной информацией о компании
    return render_template('records/record_detail.html', record=record)