# Generated by Django 2.2.4 on 2019-08-08 20:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0017_auto_20190807_2153'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Document',
        ),
    ]
