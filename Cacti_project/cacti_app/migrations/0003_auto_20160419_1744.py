# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-19 17:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cacti_app', '0002_auto_20160419_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleblock',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2016, 4, 19, 17, 44, 4, 411077, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scheduleblock',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2016, 4, 19, 17, 44, 4, 411038, tzinfo=utc)),
        ),
    ]
