# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-04 06:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]
