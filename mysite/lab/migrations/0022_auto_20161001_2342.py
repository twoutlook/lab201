# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0021_auto_20161001_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='teamid',
            field=models.IntegerField(default=1, unique=True, verbose_name='組別編號'),
        ),
    ]
