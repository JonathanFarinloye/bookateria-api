from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()


urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
]

urlpatterns += router.urls
