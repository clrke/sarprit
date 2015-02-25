from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<with_additional_data>'
    help = 'Gets accuracy of sarprit. Input anything after the command to execute analysis without clues.'

    def handle(self, *args, **options):
        from sarprit.statistics import get_accuracies

        if len(args) > 0:
            print('Performing sentiment analysis with additional data...')
            get_accuracies(True)
        else:
            print('Performing sentiment analysis without additional data...')
            get_accuracies(False)
