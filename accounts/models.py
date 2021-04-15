from django.db import models
from django.contrib.auth.models import User, AbstractUser
from PIL import Image
from django.db.models import Max


class User(AbstractUser):
    is_clientuser = models.BooleanField("clientuser status", default=True)
    phone = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5, blank=True)
    latitude = models.CharField(max_length=20, blank=True)
    longitude = models.CharField(max_length=20, blank=True)
    about = models.CharField(max_length=1000, blank=True)




class UserRegisterData(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="uprofile"
    )
    user_profile_image = models.ImageField(
        default="default.png", upload_to="user_profile_pics", blank=True
    )

    def __str__(self):
        return f"{self.user.username} ClientUser Profile"

    def save(self, *args, **kwargs):
        super(UserRegisterData, self).save(*args, **kwargs)
        img = Image.open(self.user_profile_image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.user_profile_image.path)

