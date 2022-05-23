import uuid
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    id = models.UUIDField(verbose_name='사용자 인덱스', primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='사용자 이름(닉네임)', max_length=30, unique=True)
    birthday = models.DateField(verbose_name='사용자 생일')
    profile_image = models.ImageField(verbose_name='프로필 사진', blank=True, upload_to="")
