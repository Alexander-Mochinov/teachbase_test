# teachbase_test
Тестовое задание Teachbase (Python)

Техническое задание
Необходимо разработать:
Client для работы с Teachbase API. 
1) Авторизация.
2) Проверка токена.
3) Отправка запросов.

Поддержать несколько ручек из Teachbase API (POST, GET). 

    some_api_url/courses/get_courses - список курсов
    some_api_url/courses/get_courses__id_ - детальное представление курса
    some_api_url/users/post_users_create - создание пользователя
    some_api_url/course_sessions/post_course_sessions__session_id__register - запись пользователя на сессию
    some_api_url/course_sessions/get_courses__course_id__course_sessions - сессии курсов

Создать модель курса с сохранение данных из Teachbase (*).
DRF. Реализовать ручку для получения данных курса из модели Django (*).
    1) Список всех курсов - /courses/
    2) Детальное представление курса - /courses/<id>

Flow проверки задания:
    1) Создаём пользователя.
    2) Получаем список курсов и сессии курсов.
    3) Записываем юзера на сессию.
    4) Проверяем.


Предпочитаемый стек (минимум описан ниже):
Django 4, DRF, Postgres.



При запуске необходимо авторезироваться в системе через админ панель (Не доделана логика авторизации)
Создать файлик .env в корень проекта и заполнить след. данные:

CLIENT_SECRET_API_KEY=
CLIENT_ID_KEY=
GRANT_TYPE=client_credentials
API_HOST=

# Databases data
DATABASES_NAME= 
DATABASES_USER= 
DATABASES_PASSWORD= 
DATABASES_HOST= 
DATABASES_PORT= 
