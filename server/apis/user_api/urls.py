from django.urls import path, include
from rest_framework import routers
from .views import QuestionViewSet, AnswerViewSet, UserViewSet, EmotionViewSet

app_name = 'apis.user_api'

router = routers.DefaultRouter()
router.register('questions', QuestionViewSet)
router.register('answers', AnswerViewSet)
router.register('users', UserViewSet)
router.register('emotions', EmotionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
