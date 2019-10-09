from django.urls import path

from .views import *


urlpatterns = [
    path('',StatusAPIView.as_view()),
    path('create/',StatusCreateAPIView.as_view()),
    path('<int:pk>/',StatusDetailAPIView.as_view()),
]