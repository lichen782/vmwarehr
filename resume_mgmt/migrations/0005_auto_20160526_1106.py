# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 03:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_mgmt', '0004_user_gender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Resume',
        ),
    ]
