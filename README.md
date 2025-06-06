# YaCut
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4+-red?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![Jinja2](https://img.shields.io/badge/Jinja2-3.x-orange?logo=jinja)](https://jinja.palletsprojects.com/)
[![WTForms](https://img.shields.io/badge/WTForms-3.x-brightgreen)](https://wtforms.readthedocs.io/)
[![Flask-Migrate](https://img.shields.io/badge/Flask--Migrate-Alembic-yellow?logo=alembic)](https://flask-migrate.readthedocs.io/)

Это веб-сервис разработанный на фреймворке Flask позволяющий генерировать короткие ссылки из длинных URL адресов.
Пользователь может указать собственный короткий идентификатор для генерации ссылки или позволить сервису сгенерировать его автоматически. При обращении по короткой ссылке выполняется переадресация на исходный URL. Проект включает простой веб-интерфейс с формой и REST API.

---

### Возможности

* **Создание коротких ссылок** - генерация уникальных коротких идентификаторов для заданных длинных URL.
* **Пользовательские идентификаторы** - при желании пользователь может указать свой идентификатор вместо автоматически сгенерированного. 
* **Автоматическая генерация ID** - если пользователь не указал собственный идентификатор, сервис формирует случайный короткий код. 
* **Переадресация (redirect)** - при переходе по короткой ссылке [http://127.0.0.1:5000/<short>](http://127.0.0.1:5000/<short>) происходит перенаправление на исходный длинный URL.
* **Пользовательский веб-интерфейс** - HTML-страница с формой, где можно ввести длинную ссылку и, опционально, желаемый короткий идентификатор. После отправки формы отображается сгенерированная короткая ссылка.
* **REST API** - публичный API для создания и получения ссылок.

---

### Установка и запуск проекта

1. Клонируйте проект с [репозитория](https://github.com/KuznetcovIvan/yacut.git):
   `git clone https://github.com/KuznetcovIvan/yacut.git`

2. Перейдите в директорию с проектом:
   `cd yacut`

3. Создайте виртуальное окружение в директории проекта:
   `python -m venv venv`,
   и активируйте его:
   `venv\Scripts\activate` (для Linux/macOS: `source venv/bin/activate`)

4. Установите зависимости:
   `pip install -r requirements.txt`

5. Создайте файл `.env` в корне проекта и задайте переменные окружения.
   Пример содержимого указан в файле `.env.example`.

6. Инициализируйте базу данных с помощью миграций (при использовании Flask-Migrate/Alembic):
   `flask db upgrade`
   Если миграций нет, база `db.sqlite3` будет создана автоматически при первом запуске.

7. Запустите приложение:
   `flask run`
   Приложение запустится на [http://127.0.0.1:5000/](http://127.0.0.1:5000/). В браузере будет доступна форма создания коротких ссылок.

---

### API

YaCut предоставляет два основных эндпоинта API:

| Эндпоинт          | Метод | Описание                                  | Параметры / Тело запроса                              | Ответ                                                                                                                                     |
| --------------------- | --------- | --------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| [/api/id/](http://localhost:5000/api/id/)           | POST      | Создать новую короткую ссылку.                | JSON с полями:<br>url <br>custom_id | 201 Created <br> JSON: { "url": "[...](...)",<br>"short_link": "[http://localhost:5000/<short>](http://localhost:5000/<short>)"}`|
| [/api/id/<short>/](http://localhost:5000/api/id/<short>/) | GET       | Получить оригинальную ссылку по короткому ID. | Параметр пути:<br>short_id - идентификатор ссылки       | 200 OK <br> JSON: { "url": "[...](...)"}                                                                   |

Примеры запросов к API, варианты ответов и ошибок приведены в спецификации [openapi.yml](https://github.com/KuznetcovIvan/yacut/blob/834cc6ebaa4a68560c1632b412e86cc4bad01c8f/openapi.yml).

---

### Технологический стек
- Python 
- Flask
- SQLAlchemy
- Jinja2
- WTForms
- Flask-Migrate (Alembic)

---

### Автор: [Иван Кузнецов](https://github.com/KuznetcovIvan)