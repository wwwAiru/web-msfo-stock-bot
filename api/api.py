from flask import Blueprint, jsonify, request
from models import Records, ApiKey
from app import app, data_base
from functools import wraps



api = Blueprint('api', __name__)

# декоратор проверки токена доступа к API
def require_api_key(func):
    @wraps(func)
    def check_key(*args, **kwargs):
        content_type = request.headers.get('Content-Type')
        incoming_key = request.headers.get('api-key')
        app_api_keys = [x.key for x in data_base.session.query(ApiKey.key).distinct()]
        if content_type == 'application/json':
            if incoming_key not in app_api_keys:
                return jsonify(error="ключ не валидный")
        else:
            return 'Неподдерживаемый тип контента'
        return func(*args, **kwargs)
    return check_key



# api роут для получения списка всех компаний из б.д.
@api.route('/v1/company_list', methods=['POST'])
@require_api_key
def company_list():
    records = Records.query.order_by(Records.company_name.asc())
    to_list = []
    for i in records.all():
        to_list.append(i.company_name)
    return jsonify(company_list=to_list)


# api роут для получения краткого или полного отчёта
@api.route('/v1/company_info', methods=['POST'])
@require_api_key
def company_info():
    c_name = request.get_json()
    company = Records.query.filter(Records.company_name.contains(c_name["company_name"])).first_or_404()
    if "info" in c_name.keys() and c_name["info"] == "short_info":
        return jsonify(info=company.short_info)
    elif "info" in c_name.keys() and c_name["info"] == "long_info":
        return jsonify(info=company.long_info)
    else:
        return jsonify(error="не указана пара ключ-значение, пример: 'info':'short_info' ")


