from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, min_length=8, max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True},
                        'confirm_password': {'write_only': True}}

    def validate(self, attrs):
        if len(attrs.get('password')) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters')
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError('Passwords do not match.')
        return attrs

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'], first_name=validated_data['first_name'],
                                   last_name=validated_data['last_name'], username=validated_data['username'],
                                   password=make_password(validated_data['password']))
        return user
