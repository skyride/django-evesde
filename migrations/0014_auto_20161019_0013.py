# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evesde', '0013_auto_20161018_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invmarketgroup',
            name='parentGroupID',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
