from django.shortcuts import render
from . import api
from sarprit.architecture import classify

def home(request, restaurant):
	reviews = api.search(restaurant)

	positives = []
	negatives = []
	neutrals = []

	for review in reviews:
		print(review.text)
		prediction = classify(review.text)

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
		})
