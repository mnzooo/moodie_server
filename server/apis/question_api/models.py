from django.db import models

# Create your models here.
from apis.user_auth.models import UserProfile

class Question(models.Model):
    id = models.AutoField(verbose_name='질문 인덱스', primary_key=True)
    title = models.CharField(verbose_name='질문 제목', max_length=200, null=False, default='')