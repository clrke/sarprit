# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_auto_20141112_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='current',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
