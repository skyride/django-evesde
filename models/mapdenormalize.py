from __future__ import unicode_literals

from django.db import models

class MapDenormalize(models.Model):
    itemID = models.IntegerField(primary_key=True)
    typeID = models.ForeignKey("InvType", null=True)
    groupID = models.ForeignKey("InvGroup", null=True)
    solarSystemID = models.ForeignKey("SolarSystem", null=True)
    constellationID = models.ForeignKey("Constellation", null=True)
    regionID = models.ForeignKey("Region", null=True)
    orbitID = models.IntegerField(null=True)
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    z = models.FloatField(null=True)
    radius = models.FloatField(null=True)
    itemName = models.CharField(max_length=100, null=True)
    security = models.FloatField(null=True)
    celestialIndex = models.IntegerField(null=True)
    orbitIndex = models.IntegerField(null=True)

    def __str__(self):
        return "<MapDenormalize id=%d, name='%s', typeID=%d>" % (self.itemID, self.itemName, self.typeID.typeID)
