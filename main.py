from app import app
from app import data_base
from records.blueprint import records
import view



# регистрация блюпринта арг: экземпляр класса, путь до блюпринта
app.register_blueprint(records, url_prefix='/records')

if __name__ == '__main__':
    app.run()