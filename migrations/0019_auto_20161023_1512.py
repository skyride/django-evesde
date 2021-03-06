# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evesde', '0018_mapdenormalize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constellation',
            name='regionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='constellations', to='evesde.Region'),
        ),
        migrations.AlterField(
            model_name='invgroup',
            name='categoryID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invGroups', to='evesde.InvCategory'),
        ),
        migrations.AlterField(
            model_name='invtype',
            name='groupID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invTypes', to='evesde.InvGroup'),
        ),
        migrations.AlterField(
            model_name='invtype',
            name='marketGroupID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invTypes', to='evesde.InvMarketGroup'),
        ),
        migrations.AlterField(
            model_name='solarsystem',
            name='constellationID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solarSystems', to='evesde.Constellation'),
        ),
        migrations.AlterField(
            model_name='solarsystem',
            name='regionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solarSystems', to='evesde.Region'),
        ),
    ]
