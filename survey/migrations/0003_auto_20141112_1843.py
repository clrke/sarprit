# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20141112_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='section',
            field=models.ForeignKey(to='survey.Section', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sentence',
            name='clue',
            field=models.CharField(max_length=1),
            preserve_default=True,
        ),
    ]
