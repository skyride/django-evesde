from __future__ import unicode_literals

from django.db import models

class InvGroup(models.Model):
    groupID = models.IntegerField(primary_key=True)
    categoryID = models.ForeignKey("InvCategory", related_name="invGroups", on_delete=models.CASCADE)
    groupName = models.CharField(max_length=100, db_index=True)
    iconID = models.IntegerField(null=True)
    useBasePrice = models.NullBooleanField()
    anchored = models.NullBooleanField()
    anchorable = models.NullBooleanField()
    fittableNonSingleton = models.NullBooleanField()
    published = models.NullBooleanField()


    def __unicode__(self):
        return self.groupName


    def __str__(self):
        return "<InvGroup id=%d, name='%s'>" % (self.groupID, self.groupName)
