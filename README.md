- install deps
```bash
poetry install --no-root
```

- populate db with test data and download example pics:
```bash
poetry run python ./manage.py throw_test_data
```

- runserver:
```bash
poetry run python ./manage.py runserver 9000
```

- take screenshots from templates:
```bash
poetry run python ./test/screenshot.py
```