from rest_framework import serializers
from .models import User, Answer, Question, Emotion

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = '__all__'
