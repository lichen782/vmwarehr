# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_mgmt', '0009_resume_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.CharField(default='Received', editable=False, max_length=1),
        ),
    ]
