# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20141112_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sentence',
            old_name='sentiment',
            new_name='rating',
        ),
    ]
