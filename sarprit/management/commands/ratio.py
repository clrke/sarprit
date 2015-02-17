from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Gets ratio of clues with each other.'

    def handle(self, *args, **options):
        from sarprit.statistics import get_data_ratio
        get_data_ratio()
