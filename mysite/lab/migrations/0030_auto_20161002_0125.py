# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0029_request'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': '实验申请信息', 'verbose_name_plural': '实验申请信息'},
        ),
        migrations.RemoveField(
            model_name='request',
            name='expend',
        ),
        migrations.RemoveField(
            model_name='request',
            name='expstart',
        ),
        migrations.AddField(
            model_name='request',
            name='endtime',
            field=models.DateTimeField(null=True, verbose_name='end时间'),
        ),
        migrations.AddField(
            model_name='request',
            name='starttime',
            field=models.DateTimeField(null=True, verbose_name='start时间'),
        ),
    ]
