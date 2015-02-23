from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Gets the conjunctions tagged by the system.'

    def handle(self, *args, **options):
        from sarprit.architecture import get_conjunctions

        print(get_conjunctions())
