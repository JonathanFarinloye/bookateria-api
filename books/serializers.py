from rest_framework import serializers
from .models import *


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'author', 'description', 'upload_date', 'megabytes', 'image', 'pdf',
                  'downloads', 'uploaded_by', 'all_tags', 'category', 'typology')
        read_only_fields = ('id', 'uploader', 'upload_date', 'size')
        extra_kwargs = {'typology': {'write_only': True}}


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
