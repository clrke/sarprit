# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20141112_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='sentences',
        ),
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.AddField(
            model_name='review',
            name='namedrop',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='overall_sentiment',
            field=models.CharField(default=4, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='reviews',
            field=models.ForeignKey(to='survey.Student', default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='should_display',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='student_no',
            field=models.CharField(default=1, max_length=16),
            preserve_default=False,
        ),
    ]
