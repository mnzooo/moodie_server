from django.db import transaction
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Question
from .serializer import QuestionSerializer, QuestionListSerializer

# Create your views here.
class QuestionList(APIView):
    @swagger_auto_schema(
        tags=['질문 목록'],
        query_serializer=QuestionListSerializer,
    )
    @transaction.atomic
    def get(self, request, format=None):
        question = Question.objects.all()
        serializer = QuestionListSerializer(question, many=True)
        return Response(serializer.data)

class QuestionPost(GenericAPIView):
    serializer_class = QuestionSerializer

    @swagger_auto_schema(
        tags=['질문 작성'],
        request_body=QuestionSerializer,
    )
    @transaction.atomic
    def post(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDetail(GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_object(self, pk):
        return get_object_or_404(Question, pk=pk)

    @transaction.atomic
    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    @swagger_auto_schema(
        tags=['질문 수정'],
        request_body=QuestionSerializer,
    )
    @transaction.atomic
    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['질문 삭제'],
        request_body=QuestionSerializer,
    )
    @transaction.atomic
    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
