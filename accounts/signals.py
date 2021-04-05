from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserRegisterData


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        if user.is_clientuser:
            UserRegisterData.objects.create(user=user)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    user = instance

    if user.is_clientuser:
        instance.uprofile.save()
