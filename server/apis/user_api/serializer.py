from rest_framework import serializers
from .models import UserProfile

class ProfileListSerializer(serializers.Serializer):
    name = serializers.CharField(help_text='닉네임', required=False)
    birthday = serializers.DateField(help_text='생일', required=False)
    profileImage = serializers.ImageField(help_text='프로필 사진', required=False)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'birthday', 'profile_image']

class UIDSerializer(serializers.Serializer):
    uid = serializers.CharField(help_text='uid', required=True)

class EmailLoginSerializer(serializers.Serializer):
    # 로그인 API 입력 JSON화
    email = serializers.EmailField(help_text="이메일", required=True)
    password = serializers.CharField(help_text="비밀번호", required=True)


class TokenLoginSerializer(serializers.Serializer):
    # 로그인 API 입력 JSON화
    firebase_uid = serializers.CharField(help_text="파이어베이스 uid", required=True)
