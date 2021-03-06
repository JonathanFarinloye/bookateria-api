# Generated by Django 2.2.4 on 2019-12-05 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0006_auto_20191205_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='up_votes',
        ),
        migrations.CreateModel(
            name='AUpVotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_up_votes', to='forum.Answer')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='answer_voters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='up_votes',
            field=models.ManyToManyField(related_name='a_up_voters', through='forum.AUpVotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
