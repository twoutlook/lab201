# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0053_auto_20161002_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='boardname',
            field=models.CharField(default='.', max_length=96, verbose_name='板卡名称'),
        ),
    ]
