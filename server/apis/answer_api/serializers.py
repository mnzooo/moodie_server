from .models import Answer
from rest_framework import serializers

# class AnswerSerializer(serializers.Serializer):
#     answer_content = serializers.CharField(help_text='사용자가 작성한 답변',max_length=200)

class AnswerListSerializer(serializers.Serializer):
    id = serializers.IntegerField(help_text='회원 아이디', required=False)
    answer = serializers.CharField(help_text='답변', required=False)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('question', 'answer', 'emotion')
