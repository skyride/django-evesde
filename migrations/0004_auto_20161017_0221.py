# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 02:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evesde', '0003_auto_20161017_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constellation',
            name='regionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evesde.Region'),
        ),
    ]
