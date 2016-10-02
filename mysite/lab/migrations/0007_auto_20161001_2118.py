# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0006_auto_20161001_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.CharField(default='.', max_length=16, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Teacher', verbose_name='邮箱'),
        ),
    ]