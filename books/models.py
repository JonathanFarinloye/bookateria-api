from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
import os
# Create your models here.
User = settings.AUTH_USER_MODEL


class Document(models.Model):

    def path_and_rename(self, filename):
        upload_to = 'file/'
        name = self.title + ' ' + self.author + '-bookateria.net.'
        new_name = name.replace(' ', '-') + filename.split('.')[-1]
        return os.path.join(upload_to, new_name)

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    downloads = models.IntegerField(default=0, editable=False)
    upload_date = models.DateTimeField()
    size = models.FloatField(null=True)
    image = models.ImageField(upload_to='images/', blank=True)
    pdf = models.FileField(upload_to=path_and_rename)
    uploader = models.ForeignKey(User, on_delete=models.PROTECT)
    # slug = models.SlugField(max_length=255)
    tags = models.ManyToManyField('Tag', blank=True)
    typology = models.ForeignKey('Type', on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ('title', )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + '-' + self.author)
        self.size = self.pdf.size
        if len(self.slug) >= 100:
            self.slug = self.slug[:100]
        return super(Document, self).save(*args, **kwargs)

    def megabytes(self):
        self.size = self.pdf.size
        if self.size < 1024:
            fsize = self.size
            message = str(fsize) + ' Bytes'
        elif self.size < 1048576:
            fsize = round(self.size/1024, 2)
            message = str(fsize) + ' Kb'
        else:
            fsize = round(self.size/1048576, 2)
            message = str(fsize) + ' Mb'
        return message

    def all_tags(self):
        tag_list = []
        for i in self.tags.all():
            tag_list.append(i.name)
        return tag_list

    def category(self):
        return self.typology.name

    def __str__(self):
        return self.title


class Type(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Request(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Type, related_name='request_category', on_delete=models.PROTECT)
    description = models.TextField(help_text='Anything to help find the document')

    def __str__(self):
        return self.title
