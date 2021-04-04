**Пульт охранника банка**
==================================
Pепозиторий с сайтом для урока №1 модуля "Знакомство с Django: ORM".<br/>Cайт курса: [dvman.org](https://dvmn.org/referrals/G0VoFew47MkBSuukQR1OOSmBvVF1Pa59UXhPqzZq/)

Проект представляет собой сервис по отслеживанию сотрудников банка которые посещают хранилище ценностей.  
Отслеживание ведется с помощью пропускной системы и фиксации времени входа и выхода сотрудника в базе данных.

## Запуск
* активировать виртуальное окружение с установленными зависимостями
```console
$ source venv/bin/activate
```
* запустить сайт с помощью встроенного сервера разработки
```console
$ python manage.py runserver
```


## Установка
* установить и активировать виртуальное окружение
```console
$ python3 -m venv venvх 
$ source venv/bin/activate
```
* установить зависимости
```consoleпорта
$ pip install -r requirements.txt
```
## Настройка переменных окружения
в корне проекта необходимо создать файл .env с указанием следующих переменных окружения:
  
DATABASES_NAME  - имя базы данных  
DATABASES_USER  - имя пользователя  
DATABASES_PASSWORD - пароль пользователя бaзы данных  
DATABASES_HOST - имя хоста сервера базы данных  
DATABASES_PORT - номер порта  
SECRET_KEY - секретный ключ  
DEBUG - значение параметра отладки (True или False)  
ALLOWED_HOSTS - список разрешенных хостов через запятую  
  
Пример:
```
ALLOWED_HOSTS='www.example.com, .myhost.com'
DEBUG='false'
DATABASES_USER='vasya'
```

