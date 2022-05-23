from rest_framework import serializers
from .models import User, Question, Answer

# class AnswerSerializer(serializers.Serializer):
#     answer_content = serializers.CharField(help_text='사용자가 작성한 답변',max_length=200)

from apis.answer_api.models import Answer
class AnswerSerializer(serializers.Serializer):
    class Meta:
        model = Answer
        fields = ('answer', 'emotion')