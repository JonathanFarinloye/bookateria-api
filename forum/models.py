from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL


class QuestionTags(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(QuestionTags)
    accepted_answer = models.ForeignKey('Answer', related_name='accepted', null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='question', on_delete=models.PROTECT)
    up_votes = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:20]


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    answer = models.TextField()
    up_votes = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name='answer', on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Answer to - ' + self.question.__str__()

