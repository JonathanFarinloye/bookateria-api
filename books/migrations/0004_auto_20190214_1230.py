# Generated by Django 2.1.7 on 2019-02-14 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190211_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='downloads',
            field=models.IntegerField(default=0),
        ),
    ]
