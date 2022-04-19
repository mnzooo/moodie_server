#클라이언트가 보여질
from django.urls import path
from django.conf import settings
from .views import AnswerViewSet

urlpatterns = [
    path("v1/answer", AnswerViewSet.as_view({"get":"list","post":"add"}),name="answers"),
    path("v1/answer/<int:answer_num>",AnswerViewSet.as_view({"get":"list"}),name="answer"),
]