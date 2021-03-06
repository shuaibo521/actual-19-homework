# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-31 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='主机名')),
                ('cpu_num', models.IntegerField(verbose_name='CPU核')),
                ('cpu_model', models.CharField(max_length=100, verbose_name='CPU型号')),
                ('mem_total', models.CharField(default='8G', max_length=3, verbose_name='内存')),
                ('disk', models.CharField(default='128G', max_length=4, verbose_name='磁盘大小')),
                ('public_ip', models.CharField(default='', max_length=32, verbose_name='公网ip')),
                ('private_ip', models.CharField(default='', max_length=32, verbose_name='私有ip')),
                ('remote_ip', models.CharField(default='', max_length=32, verbose_name='远程ip')),
                ('op', models.TextField(default='', max_length=32, null=True, verbose_name='运维负责人')),
                ('status', models.IntegerField(choices=[(0, '关机'), (1, '开机')], default='', verbose_name='机器状态')),
                ('os_system', models.CharField(default='', max_length=32, verbose_name='操作系统')),
                ('service_line', models.CharField(default='', max_length=32, verbose_name='所属业务线')),
                ('frame', models.CharField(default='', max_length=32, verbose_name='机架')),
                ('remark', models.TextField(default='', null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'db_table': 'assets',
            },
        ),
    ]
