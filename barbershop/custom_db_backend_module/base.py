"""
barbershop/cyrillic_case_insensitive_sqlite.py

sqlite3 из коробки не выполняет case-insensitive поиск по тексту на русском языке:
    Кудрявый == Кудрявый, но Кудрявый != кудрявый
    __icontains lookup вернёт совпадение только при совпадающих регистрах

доки джанго:
    https://docs.djangoproject.com/en/5.2/ref/databases/#substring-matching-and-case-sensitivity

нагугленное решение:
    https://docs-python.ru/standart-library/modul-sqlite3-python/sravnenie-kirillitsy-sqlite-ucheta-registra/
"""

# barbershop/custom_db_backend_module/base.py

from django.db.backends.sqlite3.base import (
    DatabaseWrapper as SQLITE3DatabaseWrapper,
)
from django.utils.asyncio import async_unsafe


class DatabaseWrapper(SQLITE3DatabaseWrapper):
    """
    Полная копия стандартного sqlite бэкенда + функция LOWERPY()
    """

    @async_unsafe
    def get_new_connection(self, conn_params):
        conn = super().get_new_connection(conn_params)
        conn.create_function("LOWERPY", 1, self.lowerpy)
        return conn

    def lowerpy(self, value):
        """
        преобразование к нижнему регистру
        """
        return value.lower()
