from django.db import models
from django.contrib.auth.models import User, AbstractUser
from PIL import Image
from django.db.models import Max
from accounts.models import UserRegisterData, User
from django.conf import settings


class Vegetable(models.Model):
    UserOwner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="vegetable")
    vegetable_name = models.CharField(max_length=80)

    def __str__(self):
        return self.vegetable_name
