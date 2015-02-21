from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Gets the count of all reviews that are not discarded.'

    def handle(self, *args, **options):
        from survey.models import Review
        print(Review.objects.all().filter(flag=2).count())
        print(Review.objects.all().filter(flag=1).count())
