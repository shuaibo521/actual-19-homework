# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20181028_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='host_status',
            field=models.IntegerField(default='', verbose_name='机器的状态0|1'),
        ),
    ]
