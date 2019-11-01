from django.db import models
# Create your models here.


class QuestionTags(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(QuestionTags)
    accepted_answer = models.ForeignKey('Answer', related_name='accepted', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title[:20]


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    answer = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    up_votes = models.IntegerField()

    def __str__(self):
        return self.question.__str__()

