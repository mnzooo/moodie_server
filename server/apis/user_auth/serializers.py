from rest_framework import serializers
import re


class EmailLoginSerializer(serializers.Serializer):
    # 로그인 API 입력 JSON화
    email = serializers.EmailField(help_text="이메일", required=True)
    password = serializers.CharField(help_text="비밀번호", required=True)


class TokenLoginSerializer(serializers.Serializer):
    # 로그인 API 입력 JSON화
    idToken = serializers.CharField(help_text="id 토큰", required=True)
