# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_mgmt', '0010_auto_20160531_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.CharField(blank=True, default='Received', max_length=200, null=True),
        ),
    ]
