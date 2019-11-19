from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()

router.register('all', UserView)

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
]

urlpatterns += router.urls
