# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_mgmt', '0014_auto_20160531_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='start_date',
            new_name='create_date',
        ),
        migrations.RemoveField(
            model_name='resume',
            name='end_date',
        ),
        migrations.AddField(
            model_name='resume',
            name='apptype',
            field=models.CharField(choices=[('Internship', 'Internship'), ('Full Time Employee', 'Full Time Employee')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='grad_year',
            field=models.IntegerField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.CharField(choices=[('Received', 'Received'), ('Pending', 'Pending'), ('Interviewed', 'Interviewed'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Received', max_length=25),
        ),
    ]
