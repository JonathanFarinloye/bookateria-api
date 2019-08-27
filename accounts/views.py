from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class ProfileView(ModelViewSet):
    http_method_names = ['get', ]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by('id')
