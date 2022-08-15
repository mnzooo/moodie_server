from django.conf import settings
from django.urls import path, include, re_path

from .views import IdTokenLogin, DummyIdToken

urlpatterns =[
    path('login/token',IdTokenLogin.as_view(), name='token_login'),
    path('dummy_token/', DummyIdToken.as_view(), name='dummy_token')
]