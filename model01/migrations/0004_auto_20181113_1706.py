# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-11-13 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model01', '0003_user_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
