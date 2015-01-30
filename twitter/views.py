from django.shortcuts import render
from . import api
from sarprit.architecture import classify
from html.parser import HTMLParser

def home(request, restaurant):
	reviews = api.search(restaurant)

	positives = []
	negatives = []
	neutrals = []
	sentences_by_clue = []

	for review in reviews:
		unescape = HTMLParser().unescape

		review.text = unescape(review.text)
		review.user.name = unescape(review.user.name)

		classification = classify(review.text)
		print(classification)

		prediction = classification[0]
		sentences_by_clue.append(classification[1])

		if prediction > 3:
			positives.append(review)
		elif prediction < 3:
			negatives.append(review)
		else:
			neutrals.append(review)

	return render(request, 'twitter/index.html',
		{
			'positives': positives, 'negatives': negatives,
			'neutrals': neutrals, 'restaurant': restaurant,
			'positives_count': len(positives) * 100 / len(reviews),
			'negatives_count': len(negatives) * 100 / len(reviews),
			'neutrals_count': len(neutrals)* 100 / len(reviews),
			'sentences_by_clue': sentences_by_clue
		})
