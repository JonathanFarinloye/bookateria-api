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


class QUpVotesView(ModelViewSet):
    serializer_class = QUpVotesSerializer
    queryset = QUpVotes.objects.all()


class AUpVotesView(ModelViewSet):
    serializer_class = AUpVotesSerializer
    queryset = AUpVotes.objects.all()