from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='users', null=True)
    emotion = models.ForeignKey('Emotion', on_delete=models.CASCADE, related_name='users', null=True)

class Question(models.Model):
    question = models.CharField(max_length=200)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='questions', null=True)
    emotion = models.ForeignKey('Emotion', on_delete=models.CASCADE, related_name='questions', null=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class Emotion(models.Model):
    emotion_name = models.CharField(max_length=20)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='emotions', null=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='emotions', null=True)
    answer = models.ForeignKey('Answer', on_delete=models.CASCADE)
