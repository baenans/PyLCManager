# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-29 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_university_university_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='home_phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
