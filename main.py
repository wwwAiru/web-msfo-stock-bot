from app import app
from app import data_base
from msfo_records.content_blueprint import msfo_records
from user_profile.user_profile import user_profile
from api.api import api
import view



# регистрация блюпринта арг: экземпляр класса, путь до блюпринта
app.register_blueprint(msfo_records, url_prefix='/msfo_records')
app.register_blueprint(user_profile, url_prefix='/user_profile')
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)