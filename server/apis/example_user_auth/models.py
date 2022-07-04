from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(verbose_name='유저 닉네임', null=False, max_length=20)
    birth_date = models.DateTimeField(verbose_name="생년월일")