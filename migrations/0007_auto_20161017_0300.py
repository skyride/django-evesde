# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evesde', '0006_auto_20161017_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarsystem',
            name='radius',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='solarsystem',
            name='securityClass',
            field=models.CharField(max_length=2, null=True),
        ),
    ]