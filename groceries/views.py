from django.urls import reverse
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from accounts.models import UserRegisterData, User, UserRegisterData
from .models import Vegetable
from django.template import loader
from .forms import VegetableForm




def register(request):
    if request.method == "POST":
        form = VegetableForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.UserOwner = request.user.username
            instance.save()
            form.save()
            vegetable = form.cleaned_data.get("vegetable_name")
            messages.success(request, f"Instance Registered for {vegetable}!")
            return render(request, "groceries/vegetableRegister.html", {"form": form})

    else:
        form = VegetableForm()
    return render(request, "groceries/vegetableRegister.html", {"form": form})

