# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilum', '0012_auto_20151003_1006'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AddField(
            model_name='crime',
            name='coordinates',
            field=models.TextField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='crime',
            name='police',
            field=models.ForeignKey(default=None, to='vigilum.PoliceOfficer'),
        ),
    ]
