"""
users/forms.py
"""

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ValidationError
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    """
    login form
    """

    def __init__(self, request, *args, **kwargs):
        super().__init__()
        for field in self.fields:
            field.widget.attrs = {**field.widget.attrs, **{"class": "form-control"}}


class UserRegistrationForm(UserCreationForm):
    """
    registration form
    """

    def __init__(self, request, *args, **kwargs):
        super().__init__()
        for field in self.fields:
            field.widget.attrs = {**field.widget.attrs, **{"class": "form-control"}}

    def clean_email(self, email):
        """
        iterates through User instances
        """
        for user in User.objects.all():
            if user.email == email:
                raise ValidationError("Пользователь с таким email уже зарегестрирован")
