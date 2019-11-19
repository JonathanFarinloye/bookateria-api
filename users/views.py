from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import filters
from knox.models import AuthToken
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering_fields = ('id', 'username', 'first_name', 'last_name', 'email')
    http_method_names = ('get', 'post')


def post_function(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
        'user': UserSerializer(user, context=self.get_serializer_context()).data,
        'token': AuthToken.objects.create(user)[1]
    })


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        post_function(self, request)


class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        post_function(self, request)
