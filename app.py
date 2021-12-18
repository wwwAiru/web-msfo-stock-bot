from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
#для миграций б.д.
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object(Configuration)
data_base = SQLAlchemy(app)

#создал объект класса Migrate в качестве параметров app и data_base для их корреяции
migrate = Migrate(app, data_base)


