from __future__ import unicode_literals

from django.db import models

class Constellation(models.Model):
    regionID = models.ForeignKey("Region", on_delete=models.CASCADE)
    constellationID = models.IntegerField(primary_key=True)
    constellationName = models.CharField(max_length=100, db_index=True)
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
    radius = models.FloatField(null=True)

    def __str__(self):
        return "<Constellation id=%d, name='%s'>" % (self.constellationID, self.constellationName)
