# Generated by Django 2.1.7 on 2019-03-03 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20190228_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='size',
        ),
    ]