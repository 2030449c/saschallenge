# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilum', '0015_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='isResolved',
            field=models.IntegerField(choices=[(1, b'Active'), (2, b'Unit At The Scene'), (3, b'Resolved')]),
        ),
        migrations.AlterField(
            model_name='crime',
            name='types',
            field=models.IntegerField(choices=[(1, b'Robbery'), (2, b'Theft'), (3, b'Rape'), (4, b'Need Backup')]),
        ),
    ]
