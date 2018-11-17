# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-11 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='用户名')),
                ('sex', models.IntegerField(choices=[(0, '男'), (1, '女')], default=0, verbose_name='性别 0 | 1')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('city', models.CharField(default='', max_length=32, verbose_name='城市')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]