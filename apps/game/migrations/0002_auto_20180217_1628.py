# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-17 16:28
from __future__ import unicode_literals

import apps.game.models.competition
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180203_1456'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=128)),
                ('token', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SingleMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infra_match_message', models.CharField(blank=True, max_length=1023, null=True)),
                ('infra_token', models.CharField(blank=True, max_length=256, null=True, unique=True)),
                ('log', models.FileField(blank=True, null=True, upload_to=apps.game.models.competition.get_log_file_directory)),
                ('part1_score', models.IntegerField(blank=True, null=True)),
                ('part2_score', models.IntegerField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('running', 'Running'), ('failed', 'Failed'), ('done', 'Done'), ('waiting', 'Waiting')], default='waiting', max_length=128)),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Map')),
            ],
        ),
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'matches'},
        ),
        migrations.AlterModelOptions(
            name='teamparticipateschallenge',
            options={'verbose_name_plural': 'Team Participates In Challenges'},
        ),
        migrations.RemoveField(
            model_name='match',
            name='done',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='score',
        ),
        migrations.AddField(
            model_name='challenge',
            name='is_submission_open',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='competition',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='infra_match_message',
            field=models.CharField(blank=True, max_length=1023, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='infra_token',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='match',
            name='log',
            field=models.FileField(blank=True, null=True, upload_to=apps.game.models.competition.get_log_file_directory),
        ),
        migrations.AddField(
            model_name='match',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='teamsubmission',
            name='infra_compile_token',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='teamsubmission',
            name='status',
            field=models.CharField(choices=[('uploading', 'Uploading'), ('uploaded', 'Uploaded'), ('compiling', 'Compiling'), ('compiled', 'Compiled'), ('failed', 'Failed')], default='uploading', max_length=128),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='description',
            field=models.CharField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='title',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='competition',
            name='type',
            field=models.CharField(choices=[('elim', 'Elimination'), ('double', 'Double Elimination'), ('league', 'League'), ('friendly', 'Friendly')], max_length=128),
        ),
        migrations.AlterField(
            model_name='game',
            name='infra_token',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='match',
            name='competition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='game.Competition'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='depend_method',
            field=models.CharField(choices=[('winner', 'Winner'), ('loser', 'Loser'), ('itself', 'Itself')], max_length=128),
        ),
        migrations.AlterField(
            model_name='teamsubmission',
            name='infra_token',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='teamsubmission',
            name='language',
            field=models.CharField(choices=[('cpp', 'C++'), ('java', 'Java'), ('py3', 'Python 3')], default='java', max_length=128),
        ),
        migrations.AlterField(
            model_name='teamsubmission',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='game.TeamParticipatesChallenge'),
        ),
        migrations.AlterUniqueTogether(
            name='teamparticipateschallenge',
            unique_together=set([('team', 'challenge')]),
        ),
        migrations.AlterUniqueTogether(
            name='useracceptsteaminchallenge',
            unique_together=set([('team', 'user')]),
        ),
        migrations.AddField(
            model_name='singlematch',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='single_matches', to='game.Match'),
        ),
        migrations.AddField(
            model_name='map',
            name='competitions',
            field=models.ManyToManyField(related_name='maps', to='game.Competition'),
        ),
    ]
