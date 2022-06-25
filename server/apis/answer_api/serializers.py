from rest_framework import serializers
from apis.answer_api.models import Answer
from apis.question_api.models import Question

class AnswerListSerializer(serializers.Serializer):
    pass
    # id = serializers.IntegerField(help_text='답변 아이디', required=False)
    # question = serializers.CharField(help_text='사용자가 작성한 답변의 질문', required=False)
    # emotion = serializers.UUIDField(help_text='사용자가 작성한 감정', required=False)
    # answer = serializers.CharField(help_text='사용자가 작성한 답변',required=False)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'answer', 'emotion']