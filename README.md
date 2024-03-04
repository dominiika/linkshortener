# linkshortener

This app uses the following stack:<br/>

```commandline
Django 5.0.2
Django REST Framework 3.14.0
Vue.js 3.4.21
PostgreSQL 13.14
```

#### If you want to, you can override env variables located in .env

## Install

#### Copy .env file

```commandline
cp .env shortener_backend/shortener_backend/.env
```

#### Build images and run containers

```commandline
docker compose up --build
```

#### The app is available at http://localhost:5173/

### Add a super user to access the admin panel

```commandline
docker exec -it link-shortener-django bash
python manage.py createsuperuser
```
