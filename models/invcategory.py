from __future__ import unicode_literals

from django.db import models

class InvCategory(models.Model):
    categoryID = models.IntegerField(primary_key=True)
    categoryName = models.CharField(max_length=100, db_index=True, null=True)
    iconID = models.IntegerField(null=True)
    published = models.NullBooleanField()

    def __unicode__(self):
        return self.categoryName

    def __str__(self):
        return "<InvCategory id=%d, name='%s'>" % (self.categoryID, self.categoryName)
