"""
users/urls.py
"""

from django.urls import path
from .views import (
    UserLoginView,
    UserRegistrationView,
    UserLogoutView,
    UserDetailView,
    UserUpdateView,
    UserPasswordChangeView,
    UserPasswordChangeDoneView,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
)


urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path(
        "profile/<int:pk>/",
        UserDetailView.as_view(),
        name="profile_detail",
    ),
    path(
        "profile/<int:pk>/edit/", UserUpdateView.as_view(), name="profile_edit"
    ),
    path(
        # смена пароля
        "password_change/",
        UserPasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        # подтверждение смены пароля
        "password_change_done/",
        UserPasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        # форма запроса восстановления пароля
        "password-reset/",
        CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        # подтверждение отправки email
        "password-reset/done/",
        CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        # форма установки нового пароля
        "reset/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        # подтверждение успешного сброса
        "reset/done/",
        CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
