from rest_framework import serializers
from .models import *


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('title', 'author', 'description', 'upload_date', 'megabytes', 'image', 'pdf',
                  'downloads', 'uploaded_by', 'all_tags', 'category')
        read_only_fields = ('uploader', 'upload_date', 'size')


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
