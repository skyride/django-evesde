from __future__ import unicode_literals

from django.db import models

class InvType(models.Model):
    typeID = models.IntegerField(primary_key=True)
    groupID = models.ForeignKey("InvGroup", on_delete=models.CASCADE)
    typeName = models.CharField(max_length=100, db_index=True, null=True)
    description = models.TextField(null=True)
    mass = models.FloatField(null=True)
    volume = models.FloatField(null=True)
    capacity = models.FloatField(null=True)
    portionSize = models.IntegerField(null=True)
    raceID = models.IntegerField(null=True)
    basePrice = models.DecimalField(max_digits=19, decimal_places=4, null=True)
    published = models.NullBooleanField()
    marketGroupID = models.ForeignKey("InvMarketGroup", null=True)
    iconID = models.IntegerField(null=True)
    soundID = models.IntegerField(null=True)
    graphicID = models.IntegerField(null=True)

    def __str__(self):
        return "<InvType id=%d, name='%s'>" % (self.typeID, self.typeName)
