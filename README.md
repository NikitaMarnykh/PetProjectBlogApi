1. Первая локальная установка
  1.1 Cоздайте директорию проекта
  1.2 В папке проекта создайте виртуальное окружение c помощью следующих команд в командной строке:
     1.2.1 cd <Полный путь к папке проекта>
     1.2.2 python -m venv <Имя виртуального окружения>
     1.2.3 Активируем виртуальной окружение с помощью команды:
           .\<Имя вашего виртуального окружения>\Scripts\activate
     1.2.4 pip list - для проверки пакетов виртуального окружения
  1.3 Переходим в PyCharm и выбираем созданный проект
  1.4 Через терминал устанавливаем фреймворк DJango:
     1.4.1 pip install django
  1.5 Устанавливаем фреймворк DJango REST Framework:
     1.5.1 pip install djrestframework
  1.6 Устанавливаем фреймворк django-filter:
     1.6.1 pip install django-filter
  1.7 Установите пакет Simple JWT:
     1.7.1 pip install djangorestframework-simplejwt
2. Запуск
   2.1 Переходим в каталог Blog:
      2.1.1 cd Blog
   2.2 Выполняем миграцию:
      2.2.1 python manage.py makemigrations
   2.3 Применяем миграцию:
      2.3.1 python manage.py migrate
   2.4 Создаём суперпользователя:
      2.4.1 python manage.py createsuperuser
   2.4 Запускаем локальный сервер:
      2.4.1 python manage.py runserver
В проекте реализовано следующее:
Требования к функционалу:
1. API для блог-постов:
  1.1 Создание, чтение, обновление и удаление постов.
2. Комментарии:
  2.1 Возможность добавлять комментарии к постам для аутентифицированных пользователей с указанием автора сообщений.
  2.2 Неаутентифицированным – только чтение.
3. Аутентификация:
  3.1 Реализация системы аутентификации для разграничения доступа к функциям API. (JWT)
  3.2 Аутефикация через логин и пароль
4. Защита от чрезмерных запросов:
  4.1 Реализация механизмов защиты API от слишком большого количества запросов от одного пользователя.
5. Фильтрация:
  5.1 Внедрение возможности фильтрации данных (например, по названию поста и по имени пользователя создавшего пост) с использованием django-filter.
6. Модерация контента:
  6.1 Организовать функционал для администратора проверки постов и комментариев (Django admin).
