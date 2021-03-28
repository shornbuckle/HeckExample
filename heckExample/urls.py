"""mysite URL Configuration

This will be our central URL file

Whenever the app server is launched all of the urls that are included below will have their path included

Make sur to add the path here of any new apps if we add them.
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", include("accounts.urls")), #we want to be able to point to urls.py in our sub files
    path('admin/', admin.site.urls),
]
