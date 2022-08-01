from django.db import models

# Create your models here.
from apis.question_api.models import Question

class Answer(models.Model):
    """
        question: 하루 문답
        answer: 답변
        createdAt: 작성일
        updatedAt: 수정일
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    emotion = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


