from django.db import connections, transaction
from django.core.exceptions import ObjectDoesNotExist

from evesde.models import *

# Imports data from the fuzzworks SDE into the main ORM
class Importer():
    def __init__(self):
        self.cursor = connections["evesde"].cursor()
        # sqlite3 UTF drama workaround
        connections["evesde"].connection.text_factory = lambda x: unicode(x, "utf-8", "ignore")


    # --------------------------------------------------------------------------
    # Update everything
    def import_all_verbose(self):
        print "Updating the capritools SDE..."
        print " * Imported Item Categories: %d added, %d updated" % self.import_invcategory()
        print " * Imported Item Groups: %d added, %d updated" % self.import_invgroup()
        print " * Imported Market Groups: %d added, %d updated" % self.import_invmarketgroup()
        print " * Imported Item Types: %d added, %d updated" % self.import_invtype()
        print " * Imported Regions: %d added, %d updated" % self.import_region()
        print " * Imported Constellations: %d added, %d updated" % self.import_constellation()
        print " * Imported Solar Systems: %d added, %d updated" % self.import_solarsystem()
        print " * Imported Map Items: %d added, %d updated" % self.import_mapdenormalize()



    # --------------------------------------------------------------------------
    # Item Categories
    @transaction.atomic
    def import_invcategory(self):
        added = 0
        updated = 0
        pk = "categoryID"

        # Query the SDE
        self.cursor.execute("SELECT * FROM invCategories")
        results = self.cursorToDict(self.cursor)

        # Iterate through the results
        items = InvCategory.objects.in_bulk()
        existing = frozenset(map(lambda x: x.categoryID, items.values()))
        for row in results:
            if row[pk] in existing:
                # Update
                item = items[row[pk]]
                if(self.dictToObject(row, item) > 0):
                    updated += 1
                    item.save()
                continue

            # Add new object
            item = InvCategory()
            self.dictToObject(row, item)
            item.save()
            added += 1

        return (added, updated)



    # --------------------------------------------------------------------------
    # Item Groups
    @transaction.atomic
    def import_invgroup(self):
        added = 0
        updated = 0
        pk = "groupID"

        # Query the SDE
        self.cursor.execute("SELECT * FROM invGroups")
        results = self.cursorToDict(self.cursor)

        # Iterate through the results
        items = InvGroup.objects.in_bulk()
        existing = frozenset(map(lambda x: x.groupID, items.values()))
        for row in results:
            if row[pk] in existing:
                # Update
                item = items[row[pk]]
                if(self.dictToObject(row, item) > 0):
                    updated += 1
                    item.save()
                continue

            # Add new object
            item = InvGroup()
            self.dictToObject(row, item)
            item.save()
            added += 1

        return (added, updated)



    # --------------------------------------------------------------------------
    # Item Market Groups
    @transaction.atomic
    def import_invmarketgroup(self):
        added = 0
        updated = 0
        pk = "marketGroupID"

        # Query the SDE
        self.cursor.execute("SELECT * FROM invMarketGroups")
        results = self.cursorToDict(self.cursor)

        # Iterate through the results
        items = InvMarketGroup.objects.order_by("parentGroupID").in_bulk()
        existing = frozenset(map(lambda x: x.marketGroupID, items.values()))
        for row in results:
            if row[pk] in existing:
                # Update
                item = items[row[pk]]
                if(self.dictToObject(row, item) > 0):
                    updated += 1
                    item.save()
                continue

            # Add new object
            item = InvMarketGroup()
            self.dictToObject(row, item)
            item.save()
            added += 1

        return (added, updated)



    # --------------------------------------------------------------------------
    # Item Types
    @transaction.atomic
    def import_invtype(self):
        added = 0
        updated = 0
        pk = "typeID"

        # Query the SDE
        self.cursor.execute("SELECT * FROM invTypes")
        results = self.cursorToDict(self.cursor)

        # Iterate through the results
        items = InvType.objects.in_bulk()
        existing = frozenset(map(lambda x: x.typeID, items.values()))
        for row in results:
            if row[pk] in existing:
                # Update
                item = items[row[pk]]
                if(self.dictToObject(row, item) > 0):
                    updated += 1
                    item.save()
                continue

            # Add new object
            item = InvType()
            self.dictToObject(row, item)
            item.save()
            added += 1

        return (added, updated)



    # --------------------------------------------------------------------------
    # Regions
    @transaction.atomic
    def import_region(self):
        added = 0
        updated = 0
        pk = "regionID"

        # Query the SDE
        self.cursor.execute("SELECT * FROM mapRegions")
        results = self.cursorToDict(self.cursor)

        # Iterate through the results
        items = Region.objects.in_bulk()
        existing = frozenset(map(lambda x: x.regionID, items.values()))
        for row in results:
            if row[pk] in existing:
                # Update
                item = items[row[pk]]
                if(self.dictToObject(row, item) > 0):
                    updated += 1
                    item.save()
                continue

            # Add new region object
            item = Region()
            self.dictToObject(row, item)
            item.save()
            added += 1

        return (added, updated)



    # --------------------------------------------------------------------------
    # Constellations
    @transaction.atomic
    def import_constellation(self):
        added = 0
        updated = 0
        pk = "constellationID"

        # Query the SDE
        self.cursor.execute("SELECT * FROM mapConstellations")
        results = self.cursorToDict(self.cursor)

        # Iterate through the results
        items = Constellation.objects.in_bulk()
        existing = frozenset(map(lambda x: x.constellationID, items.values()))
        for row in results:
            if row[pk] in existing:
                # Update
                item = items[row[pk]]
                if(self.dictToObject(row, item) > 0):
                    updated += 1
                    item.save()
                continue

            # Add new region object
            item = Constellation()
            self.dictToObject(row, item)
            item.save()
            added += 1

        return (added, updated)



    # --------------------------------------------------------------------------
    # Solar Systems
    @transaction.atomic
    def import_solarsystem(self):
        added = 0
        updated = 0
        pk = "solarSystemID"

        # Query the SDE
        self.cursor.execute("SELECT * FROM mapSolarSystems")
        results = self.cursorToDict(self.cursor)

        # Iterate through the results
        items = SolarSystem.objects.in_bulk()
        existing = frozenset(map(lambda x: x.solarSystemID, items.values()))
        for row in results:
            if row[pk] in existing:
                # Update
                item = items[row[pk]]
                if(self.dictToObject(row, item) > 0):
                    updated += 1
                    item.save()
                continue

            # Add new region object
            item = SolarSystem()
            self.dictToObject(row, item)
            item.save()
            added += 1

        return (added, updated)



    # --------------------------------------------------------------------------
    # Denormalized Map Items
    @transaction.atomic
    def import_mapdenormalize(self):
        added = 0
        updated = 0
        pk = "itemID"

        # Query the SDE
        self.cursor.execute("SELECT * FROM mapDenormalize")
        results = self.cursorToDict(self.cursor)

        # Iterate through the results
        items = MapDenormalize.objects.in_bulk()
        existing = frozenset(map(lambda x: x.itemID, items.values()))
        for row in results:
            if row[pk] in existing:
                # Update
                item = items[row[pk]]
                if(self.dictToObject(row, item) > 0):
                    updated += 1
                    item.save()
                continue

            # Add new object
            item = MapDenormalize()
            self.dictToObject(row, item)
            item.save()
            added += 1

        return (added, updated)



    # Copy values from a dict to an object
    # Bassically this takes all columns returned from the SDE column, and copies
    # their values to the value of the attribute in the object of the same name.
    # This saves us writing a massive number of assignment statements that will
    # need to be maintained.
    # Returns the number of attributes updated
    def dictToObject(self, d, obj):
        updated = 0
        for key in d.keys():
            try:
                if(getattr(obj, key) != d[key]):
                    setattr(obj, key, d[key])
                    updated += 1
            except Exception:
                # Django appends "_id" to ForeignKey columns, try that before failing
                # We also cover the fact Django requires an instance rather than
                # a primary key for updates which causes it to fail for a completely
                # different reason but the same alternative code solves it.
                altkey = "%s_id" % key
                if(getattr(obj, altkey) != d[key]):
                    setattr(obj, altkey, d[key])
                    updated += 1
        return updated



    # Generates a dictionary array from cursor results
    # Django doesn't support DictCursor for some reason but this works around
    # that for our purposes.
    def cursorToDict(self, cursor):
        # Get an array of the column names
        keys = map(lambda x: x[0], cursor.description)

        # Iterate through the rows
        r = []
        for row in cursor:
            # Build a dictionary for the row
            d = {}
            for i, value in enumerate(row):
                d[keys[i]] = value
            r.append(d)

        return r
