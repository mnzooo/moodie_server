import uuid
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    id = models.UUIDField(verbose_name='사용자 인덱스', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='사용자 이름(닉네임)', max_length=30, unique=True)
    birthday = models.DateField(verbose_name='사용자 생일')
    profile_image = models.ImageField(verbose_name='프로필 사진', blank=True, upload_to="")


### 속성이 너무 간단하다. 옵션들을 더 넣어야함. 의미를 명확하게 할 것, 논의가 필요
# null값이 가능한지에 대한 구체적으로 적어줄 것
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
