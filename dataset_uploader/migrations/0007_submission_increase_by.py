# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-04 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset_uploader', '0006_auto_20180604_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='increase_by',
            field=models.FloatField(default=1.0),
        ),
    ]
