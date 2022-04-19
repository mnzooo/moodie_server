from django.http import JsonResponse, QueryDict
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from .models import Answer
from .serializer import AnswerSerializer


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
