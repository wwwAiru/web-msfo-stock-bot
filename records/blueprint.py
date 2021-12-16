from flask import Blueprint
from flask import render_template
from models import Records



#блюпринт кусок изолированной функциональности
#record обработчик блюпринта
records = Blueprint('records', __name__, template_folder='templates') #аргументы: название блюпринта, приложение, и путь к шаблонам

@records.route('/')
def index():
    records = Records.query.all()
    return render_template('records/index.html', records=records)

# поиск слага в б.д.
@records.route('/<slug>')
def record_detail(slug):
    record = Records.query.filter(Records.slug==slug)
    return render_template('records/record_detail.html', record=record)