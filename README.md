MsfoStockBot
============

Проект <b>MsfoStockBot</b> - это сервис для инвесторов российского фондового рынка, включает в себя веб версию и телеграм бот, который работает через api веб версии.
Перед тем как запустить проект, нужно установить все библиотеки из файла requirements.txt (набрать команду в терминале pip install -r requirements.txt).
<b>Запустить файл main.py.</b>

Версия python 3.8.6+ (на более ранних версиях не проверял).
Проект рабочий(https://msfostockweb.pythonanywhere.com/), прошу не снижать балл если Вы столкнулись с проблемами запуска. 
При регистрации, письмо с подтверждением электронной почты скорее всего попадёт в спам, ищите его там)
_________
Воспользуйтесь зарегистрированными аккаунтами для тестирования функционала:
1. Администратор - логин: admin@gmail.com пароль: admin 
2. Редактор - логин: editor@gmail.com пароль: editor 
3. Обычный пользователь - логин: user@gmail.com пароль: user  
_________
В проекте используется система ролей которая позволяет разграничить права пользователей. 

Роль <b>admin</b> предоставляет панель администратора. С помощью панели администратора можно управлять любыми данными сайта, это: назначение ролей пользователям, создать/удалить пользователя, добавить/удалить отчёт компании, добавить/удалить api ключ, изменить информацию на главной странице, изменить информацию на главной странице панели администратора. Дополнительная функция - создание тестового пользователя, присутствует в профиле администратора. Создание тестового пользователя позволяет создать профиль с простым паролем (4 любых символа), а так же не требует подтверждения электронной почты.

Роль <b>editor</b> предоставляет возможность добавлять компании и отчёты, а так же их редактировать.
_________
База данных sqlite3. Для управления базой данных используется библиотека Flask-SQLAlchemy, для регистрации и авторизации используется библиотека Flask-Security-Too, для панели администратора - Flask-Admin. css стили полностью на bootstrap.
Проект содержит API, защищённый ключом, предоставляет список компаний и информацию(краткий или полный финансовый отчёт) по каждой отдельной компании. Ключи генерируются в панели администратора, на главной странице панели администратора есть инструкция, как должен происходить запрос к API.

