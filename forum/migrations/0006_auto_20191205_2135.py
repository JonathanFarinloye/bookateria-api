# Generated by Django 2.2.4 on 2019-12-05 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0005_question_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='up_votes',
        ),
        migrations.CreateModel(
            name='QUpVotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_up_votes', to='forum.Question')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='question_voters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='up_votes',
            field=models.ManyToManyField(related_name='q_up_voters', through='forum.QUpVotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
