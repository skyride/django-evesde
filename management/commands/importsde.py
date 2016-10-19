from django.core.management.base import BaseCommand, CommandError
from evesde.importer import Importer

# Imports your fuzzworks SDE in the capritools ORM SDE
# Run this command after updating your raw SDE
class Command(BaseCommand):
    def handle(self, **options):
        importer = Importer()
        importer.import_all_verbose()
