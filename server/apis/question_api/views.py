from django.db import transaction
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .exceptions import QuestionNotFound
from .models import Question
from .serializer import QuestionSerializer

# Create your views here.
from .yasg import *


class QuestionList(GenericAPIView):
    serializer_class = QuestionSerializer

    @swagger_auto_schema(
        operation_summary='질문 목록 조회',
        responses=response_schema_for_get_question_list()
    )
    @transaction.atomic
    def get(self, request):
        serializer_class = self.get_serializer_class()
        """
        1. queryset 이라는 타입을 list형태로 바꿔준다.
        2. Question이라는 model -> dictionary
        """

        # model에서 나온 DB 값, type (queryset)
        # [<Question: 오늘의 기분은 어떤가요?>, <Question: 오늘 점심은 무엇을 먹었나요?>]
        question_list = list(Question.objects.all())
        # [{"id": "1", "질문": "질문 내용"}, {"id": "2", "질문": "질문 내용"}]
        question_list_result = []

        for question in question_list:
            print(question)
            question_id = question.id
            question_title = question.title
            question_list_result.append({"id": question_id, "title": question_title})

        return Response(data={"result": question_list_result}, status=200)


class QuestionRegister(GenericAPIView):
    """
    1. 개별 질문 조회
    2. 개별 질문 등록
    3. 개별 질문 수정
    """
    serializer_class = QuestionSerializer

    @swagger_auto_schema(
        operation_summary='질문 등록',
        request_body=QuestionSerializer,
    )
    @transaction.atomic
    def post(self, request):
        serializer_class = self.get_serializer_class()
        # request.data = {"title":"foo boo"}
        question_serializer = serializer_class(data=request.data)
        if question_serializer.is_valid():
            saved_data = question_serializer.save()
            return Response(
                data={"result": {"message": "질문 등록이 완료되었습니다.", "id": saved_data.id, "title": saved_data.title}},
                status=status.HTTP_201_CREATED)
        return Response(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(GenericAPIView):
    serializer_class = QuestionSerializer

    @swagger_auto_schema(
        operation_summary='질문 상세 조회',
        responses=response_schema_for_get_question_detail()
    )
    @transaction.atomic
    def get(self, request, question_id):
        serializer_class = self.get_serializer_class()
        question_queryset = Question.objects.filter(id=question_id)
        if question_queryset:
            question_instance = question_queryset[0]
        else:
            raise QuestionNotFound

        serializer = serializer_class(question_instance)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="질문 수정",
        request_body=QuestionSerializer,
    )
    @transaction.atomic
    def patch(self, request, question_id):
        serializer_class = self.get_serializer_class()
        question_instance = Question.objects.filter(id=question_id)[0]
        serializer = serializer_class(question_instance, data=request.data)
        if serializer.is_valid():
            modified_data = serializer.save()
            return Response(
                {"result": {"message": "질문 수정이 완료되었습니다.", "id": modified_data.id, "title": modified_data.title}},
                status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="질문 삭제",
    )
    @transaction.atomic
    def delete(self, request, question_id):
        serializer_class = self.get_serializer_class()
        question_instance = Question.objects.filter(id=question_id)[0]
        question_instance.delete()
        return Response({"result": {"message": "질문 삭제가 완료되었습니다."}}, status=200)
