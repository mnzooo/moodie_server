import sys

from django.urls.conf import path

from apis.answer_api.views import *

urlpatterns = [
    path('list/', AnswerList.as_view(), name='answer_list'),
    path('', AnswerApiView.as_view(), name='answer_provide'),
    #path(''), # pk값
]
