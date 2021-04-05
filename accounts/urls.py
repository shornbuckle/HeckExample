
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.home, name="accounts-home"),
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="accounts/home.html"),
        name="logout",
    ),
    path("profile/<username>/", views.user_profile, name="userprofile"),
    path("user/profile/", views.clientuserProfileUpdate, name="user-profile"),
]
