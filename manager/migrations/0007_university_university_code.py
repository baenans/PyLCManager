# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_auto_20160830_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='university_code',
            field=models.CharField(default='', max_length=10),
        ),
    ]
