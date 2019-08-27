from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
# Create your views here.


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')