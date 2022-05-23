from django.urls import path
from apis.question_api.views import *

urlpatterns = [
    path('question/', QuestionList.as_view(), name='question_list'),
    path('question_post/', QuestionPost.as_view(), name='question_post'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='question_detail'),
]
