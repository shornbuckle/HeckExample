from django.urls import reverse
from django.contrib import messages
from .forms import (
    ClientUpdateForm,
    ClientUserRegistrationForm,
    ClientUserUpdateForm
)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from .models import UserRegisterData, User, UserRegisterData
from django.template import loader






def home(request):
    context = {}
    return render(request, "accounts/home.html", context)



def register(request):
    if request.method == "POST":

        form = ClientUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.is_active = True
            user_type = form.cleaned_data.get("user_type")
            if user_type == "Restaurant":
                user.is_restaurant = True
            elif user_type == "User":
                user.is_clientuser = True

            user.save()



            return redirect("/login")
    else:
        form = ClientUserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def user_profile(request, username):
    clientuser = User.objects.get(username=username)
    ruser = request.user
    context = {
        "user1": clientuser,
        "ruser": ruser,
    }

    template = loader.get_template("accounts/user_profile.html")

    return HttpResponse(template.render(context, request))


@login_required
def clientuserProfileUpdate(request):
    if request.method == "POST":
        clientUserUpdateForm = ClientUserUpdateForm(request.POST, instance=request.user)
        clientUpdateForm = ClientUpdateForm(
            request.POST, request.FILES, instance=request.user.uprofile
        )
        if clientUserUpdateForm.is_valid() and clientUpdateForm.is_valid():
            clientUserUpdateForm.save()
            clientUpdateForm.save()
            messages.success(request, "Account succesfully updated!")
            return redirect("/")
    else:
        clientUserUpdateForm = ClientUserUpdateForm(instance=request.user)
        clientUpdateForm = ClientUpdateForm(instance=request.user.uprofile)

    context = {
        "clientUserUpdateForm": clientUserUpdateForm,
        "clientUpdateForm": clientUpdateForm,
    }

    return render(request, "accounts/userUpdate.html", context)



