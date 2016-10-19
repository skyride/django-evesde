from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Region(models.Model):
    regionID = models.IntegerField(primary_key=True)
    regionName = models.CharField(max_length=100, db_index=True)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    xMax = models.FloatField()
    xMin = models.FloatField()
    yMax = models.FloatField()
    yMin = models.FloatField()
    zMax = models.FloatField()
    zMin = models.FloatField()
    factionID = models.IntegerField(null=True)
    radius = models.IntegerField(null=True)

    def __str__(self):
        return "<Region id=%d, name='%s'>" % (self.regionID, self.regionName)
