from django.shortcuts import render

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from apis.answer_api.models import Answer
from apis.answer_api.serializers import AnswerSerializer, AnswerListSerializer


class AnswerList(APIView):
    serializer_class = AnswerListSerializer

    @swagger_auto_schema(
        tags=['답변 목록'],
    )

    # 답변 조회
    # input은 질문, 사용자 제외
    def get(self, request):
        # request_body = request.data # 요청이 오면 json, request_body에 있는 값을 담음.
        answers = Answer.objects.all()
        # json타입으로 변경하기 .data
        serializeded_data = AnswerSerializer(answers, many=True).data

        return Response(serializeded_data, status=HTTP_200_OK)

class AnswerApiView(GenericAPIView):
    '''
    답변 API (등록, 수정, 조회)
    - 하루 문답에 대한 답변을 저장
    - 작성일과 수정일 기록 필요
    '''

    @swagger_auto_schema(
        tags=['답변 등록'],
        request_body=AnswerSerializer,
    )

    def post(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    # def get_object(self, pk):
    #     return get_object_or_404(Answer, pk=pk)

    def put(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)
