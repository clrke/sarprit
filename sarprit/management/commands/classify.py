from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<classification_type sentence sentence ...>'
    help = 'Classifies according to subjectivity, clue, sentiment, or overall sentiment'

    def handle(self, *args, **options):
        if len(args) < 1:
            raise CommandError("""Please specify the <classification_type>.
    [1] Subjectivity Classification
    [2] Clue Classification
    [3] Sentiment Analysis
    [4] Overall Sentiment Analysis""")
        elif len(args) < 2:
            raise CommandError("Please specify the sentences to be predicted")
        else:
            n = 1
            if args[0] == '1':
                from sarprit.examples import subjectivity_classifier
                classifier = subjectivity_classifier()
            elif args[0] == '2':
                from sarprit.examples import clues_classifier
                classifier = clues_classifier()
            elif args[0] == '3':
                from sarprit.examples import sentiment_classifier
                classifier = sentiment_classifier(args[1])
            elif args[0] == '4':
                from sarprit.examples import overall_classifier
                classifier = overall_classifier()
            else:
                raise CommandError("""Invalid classification_type: %s
    [1] Subjectivity Classification
    [2] Clue Classification
    [3] Sentiment Analysis
    [4] Overall Sentiment Analysis""" % args[0])

            if args[0] == '3':
                print(classifier.predict(args[2:]))
            elif args[0] == '4':
                print(classifier.predict(args[1:]))
            else:
                print([classifier.target_names[target] for target in classifier.predict(args[1:])])
