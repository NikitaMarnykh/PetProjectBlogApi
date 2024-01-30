<h1>BlogAPI</h1>
<ul>1. <h2> Первая локальная установка </h2>
  <li>1.1 Cоздайте директорию проекта </li>
    <li>1.2 В папке проекта создайте виртуальное окружение c помощью следующих команд в командной строке:</li>
    <li>1.2.1 cd <Полный путь к папке проекта></li>
    <li>1.2.2 python -m venv <Имя виртуального окружения></li>
    <li>1.2.3 Активируем виртуальной окружение с помощью команды: .\<Имя вашего виртуального окружения>\Scripts\activate</li>
    <li> 1.2.4 pip list - для проверки пакетов виртуального окружения</li>
  <li> 1.3 Переходим в PyCharm и выбираем созданный проект </li>
  <li> 1.4 Через терминал устанавливаем фреймворк DJango: </li>
  <li>   1.4.1 pip install django </li>
  <li> 1.5 Устанавливаем фреймворк DJango REST Framework: </li>
  <li>   1.5.1 pip install djrestframework </li>
  <li> 1.6 Устанавливаем фреймворк django-filter: </li>
  <li>   1.6.1 pip install django-filter </li>
  <li> 1.7 Установите пакет Simple JWT: </li>
  <li>  1.7.1 pip install djangorestframework-simplejwt </li>
  </ul>
<ul>2. <h2> Запуск </h2>
  <li> 2.1 Переходим в каталог Blog: </li>
     <li> 2.1.1 cd Blog </li>
  <li> 2.2 Выполняем миграцию: </li>
     <li> 2.2.1 python manage.py makemigrations </li>
  <li> 2.3 Применяем миграцию: </li>
     <li> 2.3.1 python manage.py migrate </li>
  <li> 2.4 Создаём суперпользователя: </li>
     <li> 2.4.1 python manage.py createsuperuser </li>
  <li> 2.5 Запускаем локальный сервер: </li>
     <li> 2.5.1 python manage.py runserver </li>
</ul>
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
