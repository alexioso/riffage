# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-29 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20171125_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riff',
            name='tags',
            field=models.CharField(default='', max_length=50),
        ),
    ]
