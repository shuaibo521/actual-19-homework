# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-05 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20181028_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='status',
            field=models.IntegerField(choices=[(0, '关机'), (1, '运行')], verbose_name='机器的状态0 | 1'),
        ),
    ]