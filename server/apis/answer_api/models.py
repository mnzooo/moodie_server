import uuid

from django.db import models
from apis.question_api.models import Question
from apis.user_api.models import User


class Emotion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, null=True)
    emotion = models.CharField(verbose_name='감정', max_length=200)

class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, null=True)
    content = models.CharField(verbose_name='답변', max_length=200)
    emotion = models.OneToOneField(Emotion, on_delete=models.CASCADE, null=True)
    createdAt = models.DateTimeField(verbose_name='생성일', auto_now_add=True)
    updatedAt = models.DateTimeField(verbose_name='수정일', auto_now=True)
