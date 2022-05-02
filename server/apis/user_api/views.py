from django.shortcuts import render
from .serializer import QuestionSerializer, AnswerSerializer, UserSerializer, EmotionSerializer
from .models import Question, Answer, User, Emotion
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets

# Create your views here.
# class QuestionListAPIView(APIView):
#     def get(self, request):
#         questions = Question.objects.all()
#         serializer = QuestionSerializer(questions, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EmotionViewSet(viewsets.ModelViewSet):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer
