# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilum', '0017_auto_20151003_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='isResolved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='crime',
            name='types',
            field=models.IntegerField(choices=[(1, b'Robbery'), (2, b'Theft'), (3, b'Rape')]),
        ),
    ]
