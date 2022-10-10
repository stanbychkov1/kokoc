# kokoc
<h1>Приложение по прохождению тестов-опросов.</h1>

Пользователь может проходить тесты, зарабатывать баллы. Участвовать в 
рейтинге пользователей по количеству пройденных тестов.
За баллы пользователь может изменить цвет никнейма, отображающийся в рейтинге
или же изменить цвет фона на странице профиля.

Тесты-опросы добавляются через админку.

1. Создайте файл .env в корневом каталоге со следующими переменными:
```bash
DJANGO_SECRET_KEY=<Задайте ваш секртеный ключ>
DJANGO_DEBUG=False

DOMAIN_NAME=127.0.0.0

DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_USER=<Задайте имя пользователя>
POSTGRES_PASSWORD=<Задайте пароль пользователя>
DJANGO_DATABASE_HOST=db
DJANGO_DATABASE_PORT=5432

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=<Задайте хост e-mail для отправки e-mail>
EMAIL_HOST_USER=<Задайте e-mail пользователя для отправки e-mail>
EMAIL_HOST_PASSWORD=<Задайте пароль e-mail пользователя для отправки e-mail>

DJANGO_USERNAME_ADMIN=admin
DJANGO_PASSWORD_ADMIN=admin
DJANGO_EMAIL_ADMIN=admin@admin.com
```
2. Запустите комманду ```docker-compose up --build``` в корневом каталоге приложения.

В сервис аренды автомобиля будут загружены тестовые данные, 
чтобы можно было проверить функционал.
Создан супер пользователь с данными Email: admin@admin.com и паролем:admin.