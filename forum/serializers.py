from rest_framework.serializers import ModelSerializer
from .models import *


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('up_votes', 'date_created', 'user', 'accepted_answer')


class QuestionTagSerializer(ModelSerializer):
    class Meta:
        model = QuestionTags
        fields = '__all__'
        read_only_fields = ('date_created', )


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ('date_created', 'up_votes', 'user')


class QUpVotesSerializer(ModelSerializer):
    class Meta:
        model = QUpVotes
        fields = '__all__'


class AUpVotesSerializer(ModelSerializer):
    class Meta:
        model = AUpVotes
        fields = '__all__'