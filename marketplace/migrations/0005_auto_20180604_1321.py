# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-04 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_auto_20180604_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='postings',
            field=models.ManyToManyField(blank=True, null=True, to='marketplace.Posting'),
        ),
    ]
