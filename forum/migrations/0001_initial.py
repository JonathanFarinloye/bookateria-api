# Generated by Django 2.2.4 on 2019-11-01 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('up_votes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('accepted_answer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='accepted', to='forum.Answer')),
                ('tags', models.ManyToManyField(to='forum.QuestionTags')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='forum.Question'),
        ),
    ]