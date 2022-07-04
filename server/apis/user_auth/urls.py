from django.conf import settings
from django.urls import path, include, re_path

from .views import IdTokenLogin

urlpatterns =[
    path('login/token',IdTokenLogin.as_view(), name='token_login')
]