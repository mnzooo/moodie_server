from django.db import transaction
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework import status
from apis.answer_api.models import Answer
from apis.answer_api.serializers import AnswerSerializer, EmotionSerializer

class AnswerList(GenericAPIView):
    serializer_class = AnswerSerializer
    # Todo 사용자 입력 시 조회되도록
    @swagger_auto_schema(
        operation_summary='답변 목록 조회',
    )
    @transaction.atomic
    def get(self, request):
        serializer_class = self.get_serializer_class()
        answer_list = list(Answer.objects.all())
        answer_list_result = []

        for answer in answer_list:
            answer_id = answer.id
            answer_userID = answer.userID
            answer_question = answer.question
            answer_content = answer.content
            answer_emotion = answer.emotion
            # answer_list_result.append({"id": answer_id, "userID": answer_userID, "question": answer_question, "emotion": answer_emotion, "content": answer_content})
            answer_list_result.append(
                {"id": answer_id, "question": answer_question, "emotion": answer_emotion, "content": answer_content})

        return Response(data={"result": answer_list_result}, status=200)

class EmotionRegister(GenericAPIView):
    serializer_class = EmotionSerializer

    @ swagger_auto_schema(
        operation_summary='감정 답변 등록',
        request_body=EmotionSerializer,
    )
    @transaction.atomic
    def post(self, request):
        serializer_class = self.get_serializer_class()
        emotion_serializer = serializer_class(data=request.data)
        if emotion_serializer.is_valid():
            saved_data = emotion_serializer.save()
            return Response(
                # data={"result": {"message": "감정 답변 등록이 완료되었습니다", "userID": saved_data.userID, "question": saved_data.question, "emotion": saved_data.emotion}},
                data={"result": {"message": "감정 답변 등록이 완료되었습니다", "question": saved_data.question, "emotion": saved_data.emotion}},

                status=status.HTTP_201_CREATED)
        return Response(emotion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnswerRegister(GenericAPIView):
    serializer_class = AnswerSerializer

    @swagger_auto_schema(
        operation_summary='답변 등록',
        request_body=AnswerSerializer,
    )
    @transaction.atomic
    def post(self, request):
        serializer_class = self.get_serializer_class()
        answer_serializer = serializer_class(data=request.data)
        if answer_serializer.is_valid():
            saved_data = answer_serializer.save()
            return Response(
                # data={"result": {"message": "답변 등록이 완료되었습니다.", "id": saved_data.id, "userID": saved_data.userID, "question": saved_data.question, "emotion": saved_data.emotion, "content": saved_data.content}},
                data={"result": {"message": "답변 등록이 완료되었습니다.", "id":saved_data.id, "question": saved_data.question, "content":saved_data.content}},
                status=status.HTTP_201_CREATED)
        return Response(answer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnswerDetail(GenericAPIView):
    serializer_class = AnswerSerializer

    @swagger_auto_schema(
        operation_summary='답변 상세 조회',
    )
    @transaction.atomic
    def get(self, request, answer_id):
        serializer_class = self.get_serializer_class()
        answer_queryset = Answer.objects.filter(id=answer_id)
        if answer_queryset:
            answer_instance = answer_queryset[0]
        else:
            raise print('error')

        serializer = serializer_class(answer_instance)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="답변 수정",
        request_body=AnswerSerializer,
    )

    @transaction.atomic
    def patch(self, request, answer_id):
        serializer_class = self.get_serializer_class()
        answer_instance = Answer.objects.filter(id=answer_id)[0]
        serializer = serializer_class(answer_instance, data=request.data)
        if serializer.is_valid():
            modified_data = serializer.save()
            return Response(
                # {"result": {"message": "답변 수정이 완료되었습니다.", "id": modified_data.id, "userID": modified_data.userID, "question": modified_data.question, "emotion": modified_data.emotion, "content": modified_data.content}}, status=200)
                {"result": {"message": "답변 수정이 완료되었습니다.", "id": modified_data.id, "question": modified_data.question, "emotion": modified_data.emotion, "content": modified_data.content}},
                status=200)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


