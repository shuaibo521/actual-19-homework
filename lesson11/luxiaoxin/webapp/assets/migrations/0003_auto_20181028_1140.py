# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20181028_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='cpu_model',
            field=models.CharField(default=1, max_length=128, verbose_name='CPU型号'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='cpu_num',
            field=models.IntegerField(default=1, verbose_name='CPU核数'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assets',
            name='remark',
            field=models.TextField(default='', null=True, verbose_name='备注'),
        ),
    ]