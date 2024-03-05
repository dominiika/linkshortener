# linkshortener

This application shortens URLs and stores them in the database, tracks the number of times each link is displayed, saves user agent data of the user providing the link, and stores a history of the last three shortened links in the local storage.

This app uses the following stack:<br/>

```commandline
Django 5.0.2
Django REST Framework 3.14.0
Vue.js 3.4.21
PostgreSQL 13.14
```

## Install

#### Copy .env file

```commandline
cp .env shortener_backend/shortener_backend/.env
```

Env variables located in .env are just example envs and can be overriden.

#### Build images and run containers

```commandline
docker compose up --build
```

#### The frontend app is available at http://localhost:5173/

#### The API is available at http://localhost:8000/api/

### Add a super user to access the admin panel

```commandline
docker exec -it link-shortener-django bash
python manage.py createsuperuser
```

#### The admin panel is available at http://localhost:8000/admin/
