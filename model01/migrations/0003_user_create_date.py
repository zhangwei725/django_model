# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-11-13 08:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model01', '0002_auto_20181113_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 13, 16, 52, 55, 934151)),
        ),
    ]
