# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-05 17:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cacti_app', '0002_auto_20160419_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.CharField(max_length=9),
        ),
        migrations.RemoveField(
            model_name='day',
            name='user',
        ),
        migrations.AddField(
            model_name='day',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='scheduleblock',
            name='day',
        ),
        migrations.AddField(
            model_name='scheduleblock',
            name='day',
            field=models.ManyToManyField(to='cacti_app.Day'),
        ),
        migrations.AlterField(
            model_name='scheduleblock',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2016, 5, 5, 17, 28, 33, 864000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scheduleblock',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2016, 5, 5, 17, 28, 33, 864000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scheduleblock',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
