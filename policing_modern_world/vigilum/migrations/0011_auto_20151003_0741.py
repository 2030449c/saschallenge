# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilum', '0010_merge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crime',
            old_name='type',
            new_name='types',
        ),
    ]
