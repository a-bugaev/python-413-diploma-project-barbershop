"""
users/views.py
"""

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
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
from .models import User
from .forms import (
    UserLoginForm,
    UserRegistrationForm,
    UserUpdateForm,
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

    def form_invalid(self, form):
        messages.error(self.request, "Ошибка")
        return super().form_invalid(form)


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


class UserLogoutView(LogoutView):
    """
    не видна пользователю
    """

    success_url = reverse_lazy("landing")

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy("landing")
        return super().dispatch(request, *args, **kwargs)


class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    личный кабинет
    """

    template_name = "profile_detail.html"
    model = User
    context_object_name = "user"
    login_url = "login"

    def get_object(self, queryset=None):
        return User.objects.get(id=self.kwargs["pk"])

    def test_func(self):
        return str(self.request.user) == str(self.get_object())


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    редактирование личного кабинета
    """

    template_name = "profile_update_form.html"
    form_class = UserUpdateForm
    model = User
    login_url = "login"

    def get_success_url(self):
        return reverse_lazy("profile_detail", kwargs={"pk": self.object.pk})

    def get_object(self, queryset=None):
        return User.objects.get(id=self.kwargs["pk"])

    def test_func(self):
        return str(self.request.user) == str(self.get_object())

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context = {
            **context,
            **{
                "title": "Изменить данные профиля",
                "button_text": "Сохранить изменения",
            },
        }
        return context

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.info(self.request, "Успешно")
        return result

    def form_invalid(self, form):
        messages.error(self.request, "Ошибка")
        return super().form_invalid(form)


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """
    смена пароля
    """

    template_name = "password_universal.html"
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("password_change_done")
    extra_context = {
        "title": "Смена пароля",
        "button_text": "Сохранить новый пароль",
    }

    def form_valid(self, form, *args, **kwargs):
        messages.info(self.request, "Успешно")
        return super().form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "Ошибка")
        return super().form_invalid(form, *args, **kwargs)


class UserPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    """
    подтверждение смены пароля
    """

    template_name = "password_universal.html"

    def get_context_data(self, **kwargs):
        """
        констекст шаблона
        """
        context = super(UserPasswordChangeDoneView, self).get_context_data(**kwargs)
        context = {
            **context,
            **{
                "title": "Пароль изменён",
                "button_text": "В личный кабинет",
                "button_url": reverse_lazy(
                    "profile_detail", kwargs={"pk": self.request.user.pk}
                ),
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

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.info(self.request, "Успешно")
        return result

    def form_invalid(self, form):
        messages.error(self.request, "Ошибка")
        return super().form_invalid(form)


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
                "button_url": reverse_lazy("landing"),
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
        context["form"] = self.get_form()
        context.update(
            {
                "title": "Сброс пароля",
                "button_text": "Сохранить новый пароль",
            }
        )
        return context

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.info(self.request, "Пароль успешно изменен")
        return result

    def form_invalid(self, form):
        messages.error(self.request, "Ошибка изменения пароля")
        return super().form_invalid(form)


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
                "button_text": "Войти",
                "button_url": reverse_lazy("login"),
            },
        }
        return context
