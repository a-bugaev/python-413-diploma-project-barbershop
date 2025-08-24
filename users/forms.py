"""
users/forms.py
"""

from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.forms import ValidationError, ModelForm
from django import forms
from .models import User


class UserLoginForm(AuthenticationForm):
    """
    login form
    """

    class Meta:
        model = User

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update(
                {"class": "form-control"}
            )


class UserRegistrationForm(UserCreationForm):
    """
    registration form
    """

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]

    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].widget.attrs.update(
                {"class": "form-control"}
            )
        self.fields["username"].help_text = ""
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""

    def clean_email(self):
        """
        iterates through User instances
        """

        email = self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "Пользователь с таким email уже зарегестрирован"
            )

        return email

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user


class UserUpdateForm(ModelForm):
    """
    форма редактирования личных данных
    """

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "birth_date",
            "telegram_id",
            "github_id",
        ]

    first_name: forms.CharField = forms.CharField(label="Имя")
    last_name: forms.CharField = forms.CharField(label="Фамилия")
    birth_date = forms.DateTimeField(label="Дата рождения")
    telegram_id: forms.CharField = forms.CharField(label="Телеграм ID")
    github_id: forms.CharField = forms.CharField(label="ГитХаб ID")


class UserPasswordChangeForm(PasswordChangeForm):
    """
    форма смены пароля
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            if "password" in field_name:
                self.fields[field_name].help_text = ""


class CustomPasswordResetForm(PasswordResetForm):
    """
    форма запроса восстановления пароля
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            if "password" in field_name:
                self.fields[field_name].help_text = ""


class CustomSetPasswordForm(SetPasswordForm):
    """
    форма установки нового пароля
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            if "password" in field_name:
                self.fields[field_name].help_text = ""
