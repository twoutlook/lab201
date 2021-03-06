# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0025_auto_20161001_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipid', models.CharField(max_length=16, unique=True, verbose_name='设备ID')),
                ('equipname', models.CharField(default='.', max_length=96, unique=True, verbose_name='设备名称')),
                ('equipnote', models.CharField(default='.', max_length=96, verbose_name='变量地址')),
            ],
            options={
                'verbose_name_plural': '实验设备',
                'verbose_name': '实验设备',
            },
        ),
    ]
