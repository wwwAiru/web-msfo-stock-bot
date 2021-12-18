from app import data_base
from datetime import datetime
import re



def slugify(s):
    # r сообщает интерпретатору считывать знаки и символы "как есть"
    pattern = r'[^\w+]'
    # ищет по шаблону pattern меняет на "-" в переменной s
    return re.sub(pattern, '-', s)

# Модель запросов в б.д.
class Records(data_base.Model):
    # столбцы базы
    id = data_base.Column(data_base.Integer, primary_key=True)
    company_name = data_base.Column(data_base.String(100), unique=True)
    # человекопонятные ссылки
    slug = data_base.Column(data_base.String(100), unique=True)
    # краткий отчёт
    short_info = data_base.Column(data_base.Text)
    # полный отчёт(ссылка)
    long_info = data_base.Column(data_base.String(300))
    updated = data_base.Column(data_base.DateTime, default=datetime.now().strftime("%d-%m-%Y- %H:%M:%S"))

    # *args список позиционных аргументов, **kwargs словарь именованных аргументов
    def __init__(self, *args, **kwargs):
        # вызываем конструктор клааса предка Model у класса Records
        # __init__ передаёт в конструктор класса Model аргументы с входа __init__ конструктора Records
        super(Records, self).__init__(*args, **kwargs)
        self.generate_slug()

    # создаём генератор человеко понятных ссылок
    def generate_slug(self):
        if self.company_name:
            self.slug = slugify(self.company_name)

    def __repr__(self):
        return f'<Record id: {self.id}, title: {self.company_name}>'




