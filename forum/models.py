from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL


class QuestionTags(models.Model):
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.name = ' '.join(str(self.name).strip().title().split())
        return super(QuestionTags, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(QuestionTags)
    accepted_answer = models.ForeignKey('Answer', related_name='accepted', null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='question', on_delete=models.PROTECT)
    up_votes = models.ManyToManyField(User, related_name='q_up_voters', through='QUpVotes')
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.title = ' '.join(str(self.title).strip().title().split())
        self.description = ' '.join(str(self.description).strip().capitalize().split())
        super(Question, self).save()

    def __str__(self):
        return self.title[:20]


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='question', on_delete=models.CASCADE)
    answer = models.TextField()
    up_votes = models.ManyToManyField(User, related_name='a_up_voters', through='AUpVotes')
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='answer', on_delete=models.PROTECT)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.answer = ' '.join(str(self.answer).strip().title().split())

    def __str__(self):
        return 'Answer to - ' + self.question.__str__()


class QUpVotes(models.Model):
    question = models.ForeignKey(Question, related_name='question_up_votes', on_delete=models.CASCADE)
    user = models.OneToOneField(User, related_name='question_voters', on_delete=models.CASCADE)


class AUpVotes(models.Model):
    question = models.ForeignKey(Answer, related_name='answer_up_votes', on_delete=models.CASCADE)
    user = models.OneToOneField(User, related_name='answer_voters', on_delete=models.CASCADE)
