from django.urls import path

from apis.user_api.views.auth_views import LoginView, DummyIdToken

urlpatterns = [
    path('login/token', LoginView.as_view(), name='token_login'),
    path('id-token/dummy', DummyIdToken.as_view(), name='get_dummy_id_token'),
]
