from __future__ import unicode_literals

from django.db import models

class SolarSystem(models.Model):
    regionID = models.ForeignKey("Region", related_name="solarSystems", on_delete=models.CASCADE)
    constellationID = models.ForeignKey("Constellation", related_name="solarSystems", on_delete=models.CASCADE)
    solarSystemID = models.IntegerField(primary_key=True)
    solarSystemName = models.CharField(max_length=100, db_index=True)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    xMax = models.FloatField()
    xMin = models.FloatField()
    yMax = models.FloatField()
    yMin = models.FloatField()
    zMax = models.FloatField()
    zMin = models.FloatField()
    luminosity = models.FloatField()
    border = models.BooleanField()
    fringe = models.BooleanField()
    corridor = models.BooleanField()
    hub = models.BooleanField()
    international = models.BooleanField()
    regional = models.BooleanField()
    constellation = models.NullBooleanField()
    security = models.FloatField()
    factionID = models.IntegerField(null=True)
    radius = models.FloatField(null=True)
    sunTypeID = models.IntegerField()
    securityClass = models.CharField(null=True, max_length=2)

    def __unicode__(self):
        return "%s < %s < %s" % (self.solarSystemName, self.constellationID.constellationName, self.regionID.regionName)

    def __str__(self):
        return "<SolarSystem id=%d, name='%s'>" % (self.solarSystemID, self.solarSystemName)
