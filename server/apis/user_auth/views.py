import http

import firebase_admin
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, views
from rest_framework.response import Response
from firebase_admin import auth, credentials
from rest_framework.generics import GenericAPIView

from .modules.firebase_token_generator import get_id_token
from .serializers import EmailLoginSerializer, TokenLoginSerializer
from rest_framework.status import *
import sys, os
import requests

import os, sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))


class IdTokenLogin(GenericAPIView):
    serializer_class = TokenLoginSerializer
    ROOT_DIR = os.path.dirname(os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    cred = credentials.Certificate(ROOT_DIR+"\moodie_firebase_auth_private_key.json")

    @swagger_auto_schema(
        operation_summary='토큰 로그인 API',
        operation_description='- 토큰으로 로그인 함.',
        request_body=serializer_class,
    )
    def post(self, request):

        # serializer 클래스 불러오기
        serializer_class = self.get_serializer_class()
        # serializer에 request 데이터 삽입
        serializer = serializer_class(data=request.data)

        # 토큰 유효성 검사
        if serializer.is_valid():

            # 아이디 토큰 Uid로 변환
            id_token = serializer.data['idToken']
            decoded_token = auth.verify_id_token(id_token)
            uid = decoded_token['uid']

            # uid기반으로 사용자 권한 반환
            user = auth.get_user(uid)

            # admin 권한이 없는 경우
            try:
                is_admin = user.custom_claims.get('admin')
            except:
                is_admin = None

            return Response(data={'token': uid, 'is_admin': is_admin}, status=HTTP_202_ACCEPTED)

        else:
            raise ValueError

class DummyIdToken(GenericAPIView):
    @swagger_auto_schema(
        tags=['Firebase ID 토큰'],
        operation_summary='더미 ID 토큰 발급 API',
    )
    def get(self, request):
        user_uid = "nMESHnruiDgZnAGHaPpMk0XduZo2"
        id_token = get_id_token(user_uid)
        return Response(data={'idToken': id_token}, status=HTTP_200_OK)