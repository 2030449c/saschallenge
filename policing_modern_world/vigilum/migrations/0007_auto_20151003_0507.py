# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vigilum', '0006_auto_20151003_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliceOfficer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=300)),
                ('is_operator', models.BooleanField(default=False)),
                ('last_accessed', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='police_officer',
            name='user',
        ),
        migrations.AlterField(
            model_name='crime',
            name='police',
            field=models.ForeignKey(to='vigilum.PoliceOfficer'),
        ),
        migrations.AlterField(
            model_name='record',
            name='police',
            field=models.ForeignKey(to='vigilum.PoliceOfficer'),
        ),
        migrations.DeleteModel(
            name='Police_Officer',
        ),
    ]
