import uuid

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
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
    # 감정: 문자로 (path로 이유: profile부분에 예시 존재)
    emotion = models.UUIDField(default=uuid.uuid4())
    answer = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer