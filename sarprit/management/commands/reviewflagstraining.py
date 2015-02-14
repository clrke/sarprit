from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Randomizes review flags(Training, Testing, Discarded)'

    def handle(self, *args, **options):
        from sarprit.statistics import set_review_flags_to_training

        set_review_flags_to_training()
