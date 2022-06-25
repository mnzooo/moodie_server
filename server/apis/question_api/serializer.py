from .models import Question
from rest_framework import serializers

class QuestionListSerializer(serializers.Serializer):
    id = serializers.IntegerField(help_text='질문 아이디', required=False)
    question = serializers.CharField(help_text='질문', required=False)

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question']
