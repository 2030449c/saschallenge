# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilum', '0011_auto_20151003_0740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='time',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
    ]
