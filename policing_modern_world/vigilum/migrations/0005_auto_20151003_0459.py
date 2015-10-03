# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vigilum', '0004_crimes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(choices=[(1, b'Robbery'), (2, b'Theft'), (3, b'Rape')])),
                ('address', models.CharField(max_length=300)),
                ('isResolved', models.BooleanField(default=False)),
                ('callerName', models.CharField(max_length=300)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('police', models.ForeignKey(to='vigilum.Userc')),
            ],
        ),
        migrations.RemoveField(
            model_name='crimes',
            name='police',
        ),
        migrations.DeleteModel(
            name='Crimes',
        ),
    ]
