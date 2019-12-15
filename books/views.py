from django.utils import timezone
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import *
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
User = get_user_model()


class DocumentView(ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ('typology',)
    search_fields = ('title', 'author', 'description', 'tags__name')
    ordering_fields = ('downloads', 'size', 'title', 'id', 'upload_date')
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # tags = []
        # for x in self.request.POST.getlist('tags'):
        #     if Tag.objects.filter(pk=x).exists():
        #         tag = Tag.objects.get(pk=x)
        #         tags.append(tag)
        #     else:
        #         new_list = self.request.POST.get('tags').split(',').strip()
        #         for i in new_list:
        #             Tag.objects.create(name=i)
        #             tag = Tag.objects.get(name__iexact=i)
        #             tags.append(tag)
        # user = User.objects.get(pk=self.request.user.pk)
        # user.profile.points += 6
        # user.profile.save()
        # print(tags)
        serializer.save(uploader=self.request.user, upload_date=timezone.datetime.now())


class TypeView(ReadOnlyModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all().order_by('id')
    permission_classes = [IsAuthenticatedOrReadOnly]


class TagView(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all().order_by('id')
    permission_classes = [IsAuthenticatedOrReadOnly]


class RequestView(ModelViewSet):
    serializer_class = RequestSerializer
    queryset = Request.objects.all().order_by('id')
    permission_classes = [IsAuthenticatedOrReadOnly]
