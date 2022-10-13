Tecnhologies:

- Python 3.9
- Django 3.2
- Django REST framework 3.13
- Nginx
- Docker
- Postgres
 
[http://51.250.24.224/recipes]

## How to Install & Setup YaMDb API?
1. Clone this repository:
```
git clone git@github.com:pyccy/api_yamdb.git
```
2. Cd into infra:
```
cd infra
```
3. Create .env and fill it: 
```
touch .env
```
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
4.Activate Docker on your computer. Open command line, go to the folder infra of the project and write:
```
docker-compose up --build -d
```
5. Make migrations
```
docker-compose exec web python manage.py migrate
```
6. Make superuser
```
docker-compose exec web python manage.py createsuperuser
```
7. Make static
```
docker-compose exec web python manage.py collectstatic --no-input
```
8. Make fixture
```
docker-compose exec web python manage.py dumpdata > fixtures.json
```
Navigate to the site in your local rest client: http://127.0.0.1:8000

Ссылка на сайт [http://51.250.24.224/recipes]