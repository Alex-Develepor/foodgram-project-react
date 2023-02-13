# **Foodgram**
### **Описание**

«Продуктовый помощник»: приложение, на котором пользователи публикуют рецепты кулинарных изделий, подписываться на публикации других авторов и добавлять рецепты в свое избранное. Сервис «Список покупок» позволит пользователю создавать список продуктов, которые нужно купить для приготовления выбранных блюд согласно рецепта/ов.


### **Стек**
![python version](https://img.shields.io/badge/Python-3.8-green)
![django version](https://img.shields.io/badge/Django-2.0.2-green)
![drf version](https://img.shields.io/badge/django_rest_framework-3.13-green)
![Docker](https://img.shields.io/badge/Docker--green)


### **Запуск проекта в dev-режиме**

1. Клонируйте репозиторий.

```
git clone git@github.com:Alex-Develepor/foodgram-project-react.git
```


2. Установите и активируйте виртуальное окружение
```
python -m venv venv
``` 
```
source venv/Scripts/activate
```

3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
4. В корне проекта создайте .env файл и заполните его
```
EMAIL_HOST_USER=ub1ka@yandex.ru
EMAIL_HOST_PASSWORD=123qwe
SECRET_KEY=p&l%385148kl9(vs
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
ALLOWED_HOSTS='*'
```
5. Запустите docker:
```
docker-compose up --build -d
```
6. Создайте миграции:
```
docker-compose exec web python manage.py migrate
```
7. Создайте суперпользователя
```
docker-compose exec web python manage.py createsuperuser
```
8. Создайте статику
```
docker-compose exec web python manage.py collectstatic --no-input
```


### Автор проекта 
* [Дворецкий Александр](https://github.com/Alex-Develepor)
