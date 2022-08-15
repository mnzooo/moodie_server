import sys

from django.urls.conf import path

from apis.answer_api.views import *

urlpatterns = [
    path('emotion/', EmotionRegister.as_view(), name='emotion_post'),
    path('list/', AnswerList.as_view(), name='answer_list'),
    path('', AnswerRegister.as_view(), name='answer_post'),
    path('<int:answer_id>', AnswerDetail.as_view(), name='answer_post'),
]
