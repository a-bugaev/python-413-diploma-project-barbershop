"""
users/models.py
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

# pylint: disable=no-member


class User(AbstractUser):
    """
    Имя и фамилия опциональны
    Email уникален и используется как логин
    """

    first_name: models.CharField = models.CharField(
        blank=True, verbose_name="Имя"
    )

    last_name: models.CharField = models.CharField(
        blank=True, verbose_name="Фамилия"
    )

    email: models.EmailField = models.EmailField(unique=True)

    avatar = models.ImageField(
        upload_to="avatar/",
        null=True,
        blank=True,
        verbose_name="Аватар",
    )
    birth_date: models.DateField = models.DateField(
        null=True, blank=True, verbose_name="Дата рождения"
    )
    telegram_id: models.CharField = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Телеграм ID"
    )
    github_id: models.CharField = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="ГитХаб ID"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
