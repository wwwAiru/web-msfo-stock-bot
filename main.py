from app import app
from app import data_base
from msfo_records.content_blueprint import msfo_records
import view



# регистрация блюпринта арг: экземпляр класса, путь до блюпринта
app.register_blueprint(msfo_records, url_prefix='/msfo_records')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 5000, debug=True)