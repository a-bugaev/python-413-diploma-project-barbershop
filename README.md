

```bash
#1
poetry install --no-root
#2
# create .env with valid values
#3
poetry run python ./manage.py migrate
#4
poetry run python ./manage.py throw_test_data
#5
poetry run python ./manage.py createsuperuser
#6
poetry run python ./manage.py runserver 9000
```


заметки по 45 ДЗ
Насколько я понял из 40-го дз, когда писал скрипт для ручного наполнения БД - получить дуступ к `settings.py` из стороннего скрипта не так просто, как кажется. Поэтому данные для телеграма лежат в `.env` и импортируются напрямую, в `settings.py` я их не вносил.