# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-04 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20181104_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]