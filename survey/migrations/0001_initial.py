# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('namedrop', models.CharField(max_length=50, blank=True)),
                ('overall_sentiment', models.IntegerField(max_length=1)),
                ('flag', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('course', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('section', models.CharField(max_length=3)),
                ('current', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('sentence', models.CharField(max_length=1000)),
                ('subjective', models.BooleanField(default=True)),
                ('clue', models.CharField(max_length=1)),
                ('rating', models.IntegerField(max_length=1)),
                ('review', models.ForeignKey(to='survey.Review')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('student_no', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=50)),
                ('should_display', models.BooleanField(default=True)),
                ('section', models.ForeignKey(to='survey.Section')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review',
            name='student',
            field=models.ForeignKey(to='survey.Student', null=True),
            preserve_default=True,
        ),
    ]
