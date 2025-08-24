"""
users/views.py
"""

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect
from .models import CustomUser
from .forms import (
    UserLoginForm,
    UserRegistrationForm,
    UserProfileUpdateForm,
    UserPasswordChangeForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm,
)


class UserLoginView(LoginView):
    """
    страница входа
    """

    form_class = UserLoginForm
    template_name = "login_registration.html"
    redirect_authenticated_user = True

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        context = super().get_context_data(**kwargs)
        context = {**context, **{"title": "Вход", "button_text": "Войти"}}
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy("landing")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request, "Вы успешно вошли")
        return super().form_valid(form)


class UserRegistrationView(CreateView):
    """
    страница регистрации
    """

    form_class = UserRegistrationForm
    template_name = "login_registration.html"
    success_url = reverse_lazy("landing")

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        context = super().get_context_data(**kwargs)
        context = {
            **context,
            **{"title": "Регистрация", "button_text": "Зарегестрироваться"},
        }
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy("landing")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(
            self.request,
            "Вы успешно зарегестрировались и вошли в свой новый аккаунт",
        )
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy("landing"))
        # return super().form_valid(form)


class UserLogoutView(LogoutView):
    """
    не видна пользователю
    """

    success_url = reverse_lazy("landing")

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy("landing")
        return super().dispatch(request, *args, **kwargs)


class UserProfileDetailView(
    LoginRequiredMixin, UserPassesTestMixin, DetailView
):
    """
    личный кабинет
    """

    template_name = "profile_detail.html"
    model = CustomUser
    context_object_name = "user"
    login_url = "login"

    def get_queryset(self):
        return CustomUser.objects.all()

    def test_func(self):
        return str(self.request.user) == str(self.get_object())


class UserProfileUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, UpdateView
):
    """
    редактирование личного кабинета
    """

    template_name = "profile_update_form.html"
    form_clas = UserProfileUpdateForm
    model = CustomUser
    login_url = "login"
    fields = [
        "username",
        "email",
        "avatar",
        "birth_date",
        "telegram_id",
        "github_id",
    ]

    def get_queryset(self):
        return CustomUser.objects.all()

    def test_func(self):
        return str(self.request.user) == str(self.get_object())

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        context = super().get_context_data(**kwargs)
        context = {
            **context,
            **{
                "title": "Редактирование личного кабинета",
                "button_text": "Сохранить изменения",
            },
        }
        return context


class UserPasswordChangeView(PasswordChangeView):
    """
    смена пароля
    """

    template_name = "password_universal.html"
    form_clas = UserPasswordChangeForm

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        context = super().get_context_data(**kwargs)
        context = {
            **context,
            **{
                "title": "Смена пароля",
                "button_text": "Сохранить новый пароль",
            },
        }
        return context


class CustomPasswordResetView(PasswordResetView):
    """
    форма запроса восстановления пароля
    """

    template_name = "password_universal.html"
    email_template_name = "password_reset_email.html"
    form_class = CustomPasswordResetForm

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        context = super().get_context_data(**kwargs)
        context = {
            **context,
            **{"title": "Забыли пароль?", "button_text": "Отправить"},
        }
        return context


class CustomPasswordResetDoneView(PasswordResetDoneView):
    """
    подтверждение отправки email
    """

    template_name = "password_universal.html"

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        context = super().get_context_data(**kwargs)
        context = {
            **context,
            **{
                "title": "Проверьте почту",
                "message": "Письмо с дальнейшими инструкциями отправлено на указанный e-mail адрес",
                "button_text": "На главную",
            },
        }
        return context


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """
    форма установки нового пароля
    """

    form_class = CustomSetPasswordForm
    template_name = "password_universal.html"

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        context = super().get_context_data(**kwargs)
        context = {
            **context,
            **{
                "title": "Установка пароля",
                "button_text": "Готово",
            },
        }
        return context


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """
    подтверждение успешного сброса
    """

    template_name = "password_universal.html"

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        context = super().get_context_data(**kwargs)
        context = {
            **context,
            **{
                "title": "Готово",
                "message": "Ваш пароль успешно изменён",
                "button_text": "В личный кабинет",
            },
        }
        return context
