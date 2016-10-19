# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 22:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evesde', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolarSystem',
            fields=[
                ('solarSystemID', models.IntegerField(primary_key=True, serialize=False)),
                ('solarSystemName', models.CharField(db_index=True, max_length=100)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('xMax', models.FloatField()),
                ('xMin', models.FloatField()),
                ('yMax', models.FloatField()),
                ('yMin', models.FloatField()),
                ('zMax', models.FloatField()),
                ('zMin', models.FloatField()),
                ('luminosity', models.FloatField()),
                ('border', models.BooleanField()),
                ('fringe', models.BooleanField()),
                ('corridor', models.BooleanField()),
                ('hub', models.BooleanField()),
                ('international', models.BooleanField()),
                ('regional', models.BooleanField()),
                ('constellation', models.BooleanField()),
                ('security', models.FloatField()),
                ('factionID', models.IntegerField(null=True)),
                ('radius', models.IntegerField(null=True)),
                ('sunTypeID', models.IntegerField()),
                ('securityClass', models.CharField(max_length=2)),
                ('constellationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evesde.Constellation')),
                ('regionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evesde.Region')),
            ],
        ),
    ]
