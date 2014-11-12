# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20141112_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='namedrop',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='should_display',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
