# Generated by Django 4.1.3 on 2022-12-07 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gothrow', '0005_delete_coursehole'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rounds',
            name='course',
        ),
        migrations.RemoveField(
            model_name='roundscore',
            name='rounds',
        ),
        migrations.RemoveField(
            model_name='roundscore',
            name='score',
        ),
        migrations.RemoveField(
            model_name='userscores',
            name='scores',
        ),
        migrations.RemoveField(
            model_name='userscores',
            name='user',
        ),
        migrations.DeleteModel(
            name='HoleScores',
        ),
        migrations.DeleteModel(
            name='Rounds',
        ),
        migrations.DeleteModel(
            name='RoundScore',
        ),
        migrations.DeleteModel(
            name='Scores',
        ),
        migrations.DeleteModel(
            name='UserScores',
        ),
    ]
