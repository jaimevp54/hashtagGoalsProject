# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goalsManager', '0002_auto_20160327_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='onDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
