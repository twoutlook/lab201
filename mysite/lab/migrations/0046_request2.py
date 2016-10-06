# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0045_auto_20161002_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rqsttime', models.DateField(auto_now_add=True, verbose_name='申请时间')),
                ('starttime', models.DateTimeField(null=True, verbose_name='start时间')),
                ('endtime', models.DateTimeField(null=True, verbose_name='end时间')),
                ('status', models.CharField(choices=[('申请', '申请'), ('指导老师核可', '指导老师核可'), ('审核', '审核'), ('实施', '实施'), ('完成', '完成')], default='申请', max_length=16, verbose_name='申请状态')),
                ('remarks', models.CharField(default='.', max_length=250, verbose_name='备注')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Experiment', verbose_name='实验项目')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.Student', verbose_name='用户')),
            ],
            options={
                'verbose_name': '实验申请信息(学生)',
                'verbose_name_plural': '实验申请信息(学生)',
            },
        ),
    ]