# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0050_authdevice_currentdevice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Student', verbose_name='学生'),
        ),
    ]
