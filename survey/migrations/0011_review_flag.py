# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_auto_20141212_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='flag',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
