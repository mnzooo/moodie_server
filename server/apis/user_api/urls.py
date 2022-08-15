from django.urls import path

from apis.user_api.views.profile_views import UserProfileList
from apis.user_api.views.auth_views import LoginView, DummyIdToken

urlpatterns = [
    path('profile', UserProfileList.as_view(), name='profile'),
    path('login/token', LoginView.as_view(), name='token_login'),
    path('id-token/dummy', DummyIdToken.as_view(), name='get_dummy_id_token'),
]
