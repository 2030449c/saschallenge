# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilum', '0002_auto_20151003_0440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userc',
            name='userID',
        ),
    ]
