# Generated by Django 2.2.4 on 2020-01-26 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0020_auto_20191215_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='slug',
        ),
    ]
