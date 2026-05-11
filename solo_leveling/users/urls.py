__all__ = ()

import django.contrib.auth.views
from django.urls import path

from users import views

app_name = 'users'

login_url = path(
    'login/',
    django.contrib.auth.views.LoginView.as_view(
        template_name='users/login.html',
    ),
    name='login',
)

signup_url = path(
    'signup/',
    views.signup,
    name='signup',
)

logout_url = path(
    'logout/',
    django.contrib.auth.views.LogoutView.as_view(
        template_name='users/logout.html',
    ),
    name='logout',
)

password_reset_url = path(
    'password_reset/',
    django.contrib.auth.views.PasswordResetView.as_view(
        template_name='users/password_reset.html',
    ),
    name='password_reset',
)

password_reset_done_url = path(
    'password_reset_done/',
    django.contrib.auth.views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html',
    ),
    name='password_reset_done',
)

password_reset_confirm_url = path(
    'password_reset_confirm/',
    django.contrib.auth.views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_confirm.html',
    ),
    name='password_reset_confirm',
)

password_reset_complete_url = path(
    'password_reset_complete/',
    django.contrib.auth.views.PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html',
    ),
    name='password_reset_complete',
)

password_change_url = path(
    'password_change/',
    django.contrib.auth.views.PasswordChangeView.as_view(
        template_name='users/password_change.html',
    ),
    name='password_change',
)

password_change_done_url = path(
    'password_change_done/',
    django.contrib.auth.views.PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html',
    ),
    name='password_change_done',
)

urlpatterns = [
    login_url,
    logout_url,
    signup_url,
    password_reset_url,
    password_reset_done_url,
    password_reset_confirm_url,
    password_reset_complete_url,
    password_change_url,
    password_change_done_url,
]
