from django.urls import reverse
from django.contrib import messages
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader


def home(request):
    context = {}
    return render(request, "accounts/home.html", context)