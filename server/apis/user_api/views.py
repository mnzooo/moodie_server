from django.db import transaction
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from .serializer import UserSerializer, ProfileListSerializer
from .models import UserProfile
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, GenericAPIView


class UserProfileList(APIView):
    @swagger_auto_schema(
        tags=['프로필 조회'],
    )
    @transaction.atomic
    def get(self, request, format=None):
        profile = UserProfile.objects.all()
        serializer = ProfileListSerializer(profile, many=True)
        return Response(serializer.data)

class PostProfile(GenericAPIView):
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(
        tags=['프로필 생성'],
        request_body=UserSerializer,
    )
    @transaction.atomic
    def post(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(UserProfile, pk=pk)

    @swagger_auto_schema(
        tags=['프로필 수정'],
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
        request_body=UserSerializer,
    )
    @transaction.atomic
    def delete(self, request, pk, format=None):
        profile = self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
