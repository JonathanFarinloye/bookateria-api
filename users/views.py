from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering_fields = ('id', 'username', 'first_name', 'last_name', 'email')
    http_method_names = ('get', 'post')


class LogoutView(APIView):
    def post(self, request):
        token = RefreshToken(request.META.get('HTTP_AUTHORIZATION').split(' ')[1])
        token.blacklist()
        return Response(status=status.HTTP_200_OK)
