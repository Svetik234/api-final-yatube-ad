# API для Yatube

Учебный проект — REST API для социальной платформы Yatube.

## Описание

API предоставляет доступ к публикациям, комментариям, группам и подпискам.
Реализована JWT-аутентификация, права доступа на основе авторства,
пагинация и поиск.

## Установка

1. Клонировать репозиторий:
git clone https://github.com/yandex-praktikum/api-final-yatube-ad.git
cd api-final-yatube-ad/yatube_api


2. Создать и активировать виртуальное окружение:
python -m venv venv
source venv/Scripts/activate



3. Установить зависимости:
pip install -r ../requirements.txt



4. Применить миграции:
python manage.py migrate



5. Запустить сервер:
python manage.py runserver


## Примеры запросов

Получение JWT-токена:
POST /api/v1/jwt/create/
{
"username": "user",
"password": "password"
}



Получение списка публикаций:
GET /api/v1/posts/
Authorization: Bearer <access_token>



Создание публикации:
POST /api/v1/posts/
Authorization: Bearer <access_token>
{
"text": "Текст публикации",
"group": 1
}



Получение подписок:
GET /api/v1/follow/
Authorization: Bearer <access_token>



Подписка на пользователя:
POST /api/v1/follow/
Authorization: Bearer <access_token>
{
"following": "username"
}



## Документация

После запуска сервера документация доступна по адресу:
http://127.0.0.1:8000/redoc/
