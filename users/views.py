"""
users/views.py
"""

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import UserLoginForm, UserRegistrationForm


class UserLoginView(LoginView):
    """
    страница входа
    """

    form_class = UserLoginForm
    template_name = "login_registration.html"

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        return {"title": "Вход", "button_text": "Войти"}


class UserRegistrationView(CreateView):
    """
    страница регистрации
    """

    form_class = UserRegistrationForm
    template_name = "login_registration.html"
    success_url = "landing"

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        return {"title": "Регистрация", "button_text": "Зарегестрироваться"}


class UserLogoutView(LogoutView):
    """
    не видна пользователю
    """
