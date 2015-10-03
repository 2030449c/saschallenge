# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='userc',
            old_name='is_user',
            new_name='is_operator',
        ),
        migrations.AddField(
            model_name='record',
            name='police',
            field=models.ForeignKey(to='vigilum.Userc'),
        ),
    ]
