# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 23:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0022_auto_20161001_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Team', verbose_name='組別'),
        ),
    ]
