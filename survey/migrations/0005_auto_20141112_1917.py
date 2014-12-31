# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20141112_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reviews',
            new_name='student',
        ),
        migrations.AddField(
            model_name='sentence',
            name='sentiment',
            field=models.IntegerField(default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='review',
            name='overall_sentiment',
        ),
        migrations.AddField(
            model_name='review',
            name='overall_sentiment',
            field=models.IntegerField(max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sentence',
            name='review',
            field=models.ForeignKey(to='survey.Review'),
            preserve_default=True,
        ),
    ]
