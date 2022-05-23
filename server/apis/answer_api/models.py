from django.db import models

# Create your models here.
from apis.user_api.models import User, Question

class Answer(models.Model):
    """
        userEmail: 사용자 이메일
        question: 하루 문답
        answer: 답변
        createdAt: 작성일
        updatedAt: 수정일
    """
    userEmail = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

