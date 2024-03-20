# bet-maker


# Запуск:

В корне проекта создать файл с переменными окружения на основе .env.example

docker-compose up --build -d

из контейнера с приложением выполнить миграции:
alembic revision --autogenerate -m 'initial'
alembic upgrade head

апи будет доступен по адресу:
http://0.0.0.0:8080/docs
