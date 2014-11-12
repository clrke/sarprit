# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_auto_20141112_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='subjective',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='should_display',
            field=models.BooleanField(),
            preserve_default=True,
        ),
    ]
