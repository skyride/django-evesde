# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evesde', '0012_auto_20161018_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invmarketgroup',
            name='parentGroupID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='evesde.InvMarketGroup'),
        ),
    ]
