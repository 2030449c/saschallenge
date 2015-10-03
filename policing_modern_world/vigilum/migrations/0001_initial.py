# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('types', models.IntegerField(choices=[(1, b'Robbery'), (2, b'Theft'), (3, b'Rape')])),
                ('address', models.CharField(max_length=300)),
                ('isResolved', models.BooleanField(default=False)),
                ('callerName', models.CharField(max_length=300)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('coordinates', models.TextField(max_length=200)),
            ],
        ),
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
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('police', models.ForeignKey(to='vigilum.PoliceOfficer')),
            ],
        ),
        migrations.CreateModel(
            name='ut',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='crime',
            name='police',
            field=models.ForeignKey(blank=True, to='vigilum.PoliceOfficer', null=True),
        ),
    ]
