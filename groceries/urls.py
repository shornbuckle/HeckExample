
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "groceries"
urlpatterns = [
    path("groceryStore/", views.register, name="groceryStore"),
    path("myPantry/", views.register, name="myPantry"),
]
