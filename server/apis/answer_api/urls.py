import sys

from django.urls.conf import path

from apis.answer_api.views import *

urlpatterns = [
    path('answer/', AnswerApiView.as_view(), name='answer_provide'),
]
