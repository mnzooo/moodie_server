import uuid
from django.db import models

# Create your models here.
class UserAccount(models.Model):
    id = models.UUIDField(verbose_name='사용자 계정 인덱스', primary_key=True, default=uuid.uuid4, editable=False)
    user_uid = models.CharField(verbose_name='사용자 uid', null=False, max_length=40, default='')

class UserProfile(models.Model):
    id = models.UUIDField(verbose_name='사용자 인덱스', primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.OneToOneField(UserAccount, verbose_name='사용자 uid 외래키', related_name="user_account", on_delete=models.CASCADE, db_column="user_id", default='')
    name = models.CharField(verbose_name='사용자 이름(닉네임)', max_length=30, unique=True)
    birthday = models.DateField(verbose_name='사용자 생일')
    profile_image = models.ImageField(verbose_name='프로필 사진', blank=True, upload_to="")
