# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 08:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0044_auto_20161002_0804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': '实验申请信息(老师)', 'verbose_name_plural': '实验申请信息(老师)'},
        ),
    ]