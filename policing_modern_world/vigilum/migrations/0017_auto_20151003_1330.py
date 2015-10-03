# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilum', '0016_auto_20151003_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='isResolved',
            field=models.IntegerField(default=1, choices=[(1, b'Active'), (2, b'Unit At The Scene'), (3, b'Resolved')]),
        ),
    ]
