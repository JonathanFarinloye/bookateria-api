# Generated by Django 2.1.7 on 2019-03-03 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_books_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='size',
        ),
    ]
