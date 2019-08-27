from rest_framework.viewsets import ModelViewSet
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering_fields = ('id', 'username', 'first_name', 'last_name', 'email')
