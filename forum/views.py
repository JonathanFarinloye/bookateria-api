from .serializers import *
from .models import *
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
User = get_user_model()


class QuestionView(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if self.request.data['up_votes']:
            question = Question.objects.get(pk=self.request.data['question'])
            question.up_votes += 1
            question.save()


class QuestionTagView(ModelViewSet):
    serializer_class = QuestionTagSerializer
    queryset = QuestionTags.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AnswerView(ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if self.request.data['up_votes']:
            answer = Answer.objects.get(pk=self.request.data['answer'])
            answer.up_votes += 1
            if self.request.user == answer.question.user:
                answer.question.accepted_answer = answer
            answer.save()


