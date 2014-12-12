# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0009_section_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='student',
            field=models.ForeignKey(null=True, to='survey.Student'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='section',
            name='current',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sentence',
            name='subjective',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='should_display',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
