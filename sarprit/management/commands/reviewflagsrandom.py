from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Randomizes review flags(Training, Testing, Discarded)'

    def handle(self, *args, **options):
        from sarprit.statistics import randomize_review_flags

        randomize_review_flags()
