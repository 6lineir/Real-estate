from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=12 ,verbose_name="موبایل")
    watsapp = models.CharField(max_length=12 ,blank=True, verbose_name="شماره واتس آپ")
    telegram = models.CharField(max_length=12 ,blank=True, verbose_name="شماره تلگرام")
    avatar = models.ImageField(upload_to="avatar", blank=True, verbose_name="تصویر نمایه")
