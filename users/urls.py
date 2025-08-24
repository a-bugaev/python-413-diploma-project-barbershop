"""
users/urls.py
"""

from django.urls import path
from .views import (
    UserLoginView,
    UserRegistrationView,
    UserLogoutView,
    UserProfileDetailView,
    UserProfileUpdateView,
    UserPasswordChangeView,
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
        UserProfileDetailView.as_view(),
        name="profile_detail",
    ),
    path(
        "profile/<int:pk>/edit/", UserProfileUpdateView.as_view(), name="profile_edit"
    ),
    path(
        "password_change/",
        UserPasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password-reset/",
        CustomPasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        CustomPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
