# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-19 17:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cacti_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleblock',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2016, 4, 19, 17, 19, 48, 841000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='scheduleblock',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2016, 4, 19, 17, 19, 48, 841000, tzinfo=utc)),
        ),
    ]
