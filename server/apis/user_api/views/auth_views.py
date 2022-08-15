import firebase_admin
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from firebase_admin import auth, credentials
from rest_framework.generics import GenericAPIView
from apis.user_api.serializer import UIDSerializer
from rest_framework.status import *

import os, sys

from apis.user_api.firebase_token_generator import get_id_token

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

class LoginView(GenericAPIView):
    serializer_class = UIDSerializer

    def post(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        # 토큰 유효성 검사
        if serializer.is_valid():
            uid = serializer.data['uid']
            user = auth.get_user(uid)

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
        # responses=response_schema_id_token(),
    )
    def get(self, request):
        user_uid = "nMESHnruiDgZnAGHaPpMk0XduZo2"
        id_token = get_id_token(user_uid)
        return Response(data={'idToken': id_token}, status=HTTP_200_OK)
