# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-04 17:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataset_uploader', '0007_submission_increase_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='size_in_mb',
        ),
    ]
