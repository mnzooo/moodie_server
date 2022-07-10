from django.db import models

# Create your models here.
from apis.user_auth.models import UserProfile


class Question(models.Model):
    id = models.AutoField(verbose_name='질문 인덱스', primary_key=True)
    question = models.CharField(verbose_name='질문', max_length=200)
    user = models.ManyToManyField(UserProfile, verbose_name='유저 정보 외래키', related_name='questions', blank=True, default='',
                                  db_column='user')

    def __str__(self):
        return self.question
