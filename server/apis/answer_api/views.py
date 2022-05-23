from django.shortcuts import render

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView

from apis.answer_api.models import Answer
from apis.answer_api.serializers import AnswerSerializer


class AnswerApiView(GenericAPIView):
    '''
    답변 API (등록, 수정, 조회)
    - 하루 문답에 대한 답변을 저장
    - 작성일과 수정일 기록 필요
    '''
    serializer_class = AnswerSerializer

    @swagger_auto_schema(
        operation_summary="답변 API (등록, 수정, 조회)",
        #request_body=AnswerSerializer
    )
    # 답변 조회
    # input은 질문, 사용자 제외
    def get(self, request):
        #request_body = request.data # 요청이 오면 json, request_body에 있는 값을 담음.
        answers = Answer.objects.all()
        #serializer = AnswerSerializer(answers,many=True)
        return Response(answers, status=HTTP_200_OK)

    def post(self, request):
        answers = Answer.objects.all()
        return Response(answers, status=HTTP_200_OK)

    def put(self, request):
        answers = Answer.object.all()
        return Response(answers, status=HTTP_200_OK)



