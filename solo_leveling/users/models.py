from django.db import models
import django.contrib.auth.models
from django.contrib.auth.models import User as BaseUser

class User(BaseUser):
    class Meta:
        proxy = True

class Profile(models.Model):
    user = models.OneToOneField(
        django.contrib.auth.models.User,
        on_delete=models.CASCADE,
    )

    fire_mode = models.IntegerField(
        "Ударный режим",
        default=0,
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиля'

