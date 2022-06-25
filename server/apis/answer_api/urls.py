import sys

from django.urls.conf import path

from apis.answer_api.views import *

urlpatterns = [
    path('', AnswerListView.as_view(), name='answer_provide'),
    path('<int:pk>/', AnswerDetail.as_view(), name='answer_detail'),
    path('answer_post/', AnswerPost.as_view(), name='answer_post'),
]
