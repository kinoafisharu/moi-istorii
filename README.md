# Мои Истории
### Для коллаборации:
1. Делаем fork настоящего репозитория
2. Клонируем репозиторий к себе на компьютер
3. <code>cd ./moi-istorii</code>
4. Устанавливаем виртуальное окружение (Пример на линуксе: <code>python3 -m venv venv</code>)
5. <code>pip install -r requirements.txt</code>
6. Комментируем 90, 91 строки в settings.py 
        <br><code>#import dj_database_url</code>
        <br><code>#DATABASES['default'] = dj_database_url.config(conn_max_age=600)</code>
7. <code>./manage.py migrate</code>
8. <code>./manage.py runserver</code>
<br>
Готово! Можем начинать.
