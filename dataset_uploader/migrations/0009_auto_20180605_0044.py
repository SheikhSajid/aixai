# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-04 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset_uploader', '0008_remove_submission_size_in_mb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='increase_by',
            field=models.CharField(default='1X', max_length=3),
        ),
    ]
