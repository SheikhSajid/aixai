# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-04 06:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.UserProfileInfo')),
            ],
        ),
    ]