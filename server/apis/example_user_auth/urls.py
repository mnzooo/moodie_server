from django.urls import path

from apis.user_api.views import *

urlpatterns = [
    path('profile', UserProfileList.as_view(), name='profile'),
    path('profile_post', PostProfile.as_view(), name='post_profile'),
    path('profile/<uuid:pk>/', ProfileDetail.as_view(), name='profile_detail'),
]
