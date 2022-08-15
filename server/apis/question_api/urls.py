from django.urls import path
from apis.question_api.views import *

urlpatterns = [
    path('list', QuestionList.as_view(), name='question_list'),
    path('', QuestionRegister.as_view(), name='question_post'),
    path('<int:question_id>', QuestionDetail.as_view(), name='question_post'),
]
