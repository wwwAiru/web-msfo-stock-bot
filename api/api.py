from flask import Blueprint, jsonify, request
from models import Records, ApiKey
from app import app, data_base
from functools import wraps



api = Blueprint('api', __name__)

# декоратор проверки токена доступа к API
def require_api_token(func):
    @wraps(func)
    def check_token(*args, **kwargs):
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            incoming_key = request.headers.get('api_session_token')
            app_api_key = ApiKey.query.filter(ApiKey.key == incoming_key).first()
            if incoming_key != str(app_api_key):
                return jsonify(error='доступ запрещён')
        else:
            return 'Неподдерживаемый тип контента'
        return func(*args, **kwargs)
    return check_token



# api роут для получения списка всех компаний из б.д.
@api.route('/v1/company_list/', methods=['POST', 'GET'])
@require_api_token
def company_list():
    records = Records.query.order_by(Records.company_name.asc())
    to_list = []
    for i in records.all():
        to_list.append(i.company_name)
    return jsonify(company_list=to_list)
    #return render_template('test.html', records=records)