# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilum', '0013_auto_20151003_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crime',
            name='police',
            field=models.ForeignKey(blank=True, to='vigilum.PoliceOfficer', null=True),
        ),
    ]
