Данное приложение представляет собой трекер полезных привычек
Для его работы необходимо выполнить следующее:
1. Ввести в консоль команду python manage.py runserver;
2. Внести в БД привычки через postman, админку или фикстуру;
3. Ввести в консоль команду celery -A config worker -l INFO -P eventlet для запуска оправки сообщений в телеграм бота