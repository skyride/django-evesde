from __future__ import unicode_literals

from django.db import models

class InvMarketGroup(models.Model):
    marketGroupID = models.IntegerField(primary_key=True)
    parentGroupID = models.IntegerField(null=True, blank=True)
    marketGroupName = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=3000, null=True)
    iconID = models.IntegerField(null=True)
    hasTypes = models.NullBooleanField()

    def __unicode__(self):
        return self.marketGroupName

    def __str__(self):
        return "<InvMarketGroup id=%d, name='%s'>" % (self.marketGroupID, self.marketGroupName)
