from django.db import transaction
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from apis.user_api.serializer import UserSerializer, ProfileListSerializer
from apis.user_api.models import UserProfile
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, GenericAPIView

class UserProfileList(GenericAPIView):
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(
        tags=['프로필 조회'],
    )
    @transaction.atomic
    def get(self, request, format=None):
        profile = UserProfile.objects.all()
        serializer = ProfileListSerializer(profile, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        tags=['프로필 생성'],
        operation_description='프로필을 생성함',
        request_body=ProfileListSerializer,
    )
    @transaction.atomic
    def post(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['프로필 수정'],
        operation_description='프로필을 수정함',
        request_body=UserSerializer,
    )
    @transaction.atomic
    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = UserSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['프로필 삭제'],
        operation_description='프로필을 삭제함',
        request_body=UserSerializer,
    )
    @transaction.atomic
    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
