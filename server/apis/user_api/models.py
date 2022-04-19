from django.db import models

# Create your models here.
class User(models.Model):
    """
        userEmail: 사용자 이메일
        name: 사용자 이름
        password: 사용자 비밀번호
    """
    userEmail = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Question(models.Model):
    """
        question: 하루 문답
    """
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question

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