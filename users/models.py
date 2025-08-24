"""
users/models.py
"""

from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    """
    add email field to default model
    """

    avatar: models.ImageField = models.ImageField(null=True, blank=True)
    birth_date: models.DateTimeField = models.DateTimeField(
        null=True, blank=True
    )
    telegram_id: models.CharField = models.CharField(null=True, blank=True)
    github_id: models.CharField = models.CharField(null=True, blank=True)
