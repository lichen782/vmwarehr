# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_mgmt', '0017_auto_20160531_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]