# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0030_auto_20161002_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('申请', '申请'), ('审核', '审核'), ('实施', '实施'), ('完成', '完成')], default='申请', max_length=99, verbose_name='申请状态'),
        ),
    ]
