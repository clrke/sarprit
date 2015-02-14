from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<without_clues>'
    help = 'Gets accuracy of sarprit. Input anything after the command to execute analysis without clues.'

    def handle(self, *args, **options):
        from sarprit.statistics import get_accuracy

        if len(args) > 0:
            print('Performing sentiment analysis without clues classification...')
            get_accuracy(True)
        else:
            print('Performing sentiment analysis with clues classification...')
            get_accuracy(False)
