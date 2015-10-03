# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vigilum', '0008_remove_policeofficer_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='policeofficer',
            name='username',
            field=models.CharField(default=datetime.datetime(2015, 10, 3, 4, 15, 9, 367000, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
    ]
