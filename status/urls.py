from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import *


urlpatterns = [
    path('',StatusAPIView.as_view()),
    path('auth/jwt/',obtain_jwt_token),
    path('token/refresh/',refresh_jwt_token),
    path('create/',StatusCreateAPIView.as_view()),
    path('<int:pk>/',StatusDetailAPIView.as_view()),
]