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
from .models import CustomUser


class UserLoginForm(AuthenticationForm):
    """
    login form
    """

    class Meta:
        model = CustomUser

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
        model = CustomUser
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

        if CustomUser.objects.filter(email=email).exists():
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


class UserProfileUpdateForm(ModelForm):
    """
    форма редактирования личных данных
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "avatar",
            "birth_date",
            "telegram_id",
            "github_id",
        ]
        labels = {
            "avatar": "Аватар",
        }

    birth_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"class": "form-control"}),
        label="Дата рождения",
    )

    avatar: forms.ImageField = forms.ImageField(label="Аватар")


class UserPasswordChangeForm(PasswordChangeForm):
    """
    форма восстановления пароля
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].help_text = ""
        print(self.fields.keys())


class CustomPasswordResetForm(PasswordResetForm):
    """
    форма восстановления пароля
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].help_text = ""
        print(self.fields.keys())


class CustomSetPasswordForm(SetPasswordForm):
    """
    форма восстановления пароля
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields.keys():
            self.fields[field_name].help_text = ""
        print(self.fields.keys())
