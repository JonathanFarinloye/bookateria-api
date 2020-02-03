from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from django.core import exceptions
import django.contrib.auth.password_validation as validators

User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email', 'password')
    #     extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        # here data has all the fields which have validated values
        # so we can create a User instance out of it
        user = User(**data)

        # get information from data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        errors = dict()

        if username and password and email:
            if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
                error = {
                    'status': False,
                    'message': 'Email or Username already exists.'
                }
                raise serializers.ValidationError(error)
            else:
                try:
                    validators.validate_password(password=password, user=User)
                except exceptions.ValidationError as e:
                    errors['password'] = list(e.messages)

                if errors:
                    raise serializers.ValidationError(errors)
                else:
                    return super(RegisterSerializer, self).validate(data)
        else:
            error = {
                'status': False,
                'message': 'Details not found in request.'
            }
            raise serializers.ValidationError(error, code='authorization')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)

        username = data.get('username')
        password = data.get('password')

        if username and password:
            if User.objects.filter(username=username).exists():
                user = authenticate(request=self.context.get('request'), username=username, password=password)
            else:
                error = {
                    'status': False,
                    'message': 'User does not exist'
                }
                raise serializers.ValidationError(error)

            if not user:
                error = {
                    'status': False,
                    'message': 'Invalid Credentials'
                }

                raise serializers.ValidationError(error, code='authorization')

        else:
            error = {
                'status': False,
                'message': 'Details not found in request'
            }
            raise serializers.ValidationError(error, code='authorization')

        data['user'] = user
        return data['user']
        # if user and user.is_active:
        #     return user
        # raise serializers.ValidationError("Wrong Credentials")
