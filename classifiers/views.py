from django.shortcuts import render
from sarprit.shortcuts import to_json
from sarprit.examples import classifier1, classifier2, classifier3a, classifier3b, classifier3c, classifier3d, classifier4
from sarprit.feature_extraction import extract

def home(request):
	return render(request, 'classifiers/index.html',
		{
			'classifier1' : { 'feature_names': classifier1.feature_names, 'data': [(classifier1.features[i], classifier1.target[i]) for i in range(len(classifier1.features))] },
			'classifier2' : { 'feature_names': classifier2.feature_names, 'data': [(classifier2.features[i], classifier2.target[i]) for i in range(len(classifier2.features))] },
			'classifier3a' : classifier3a,
			'classifier3b' : classifier3b,
			'classifier3c' : classifier3c,
			'classifier3d' : classifier3d,
			'classifier4' : classifier4,
		})
def subjectivity(request, id, sentence):
	is_subjective = classifier1.predict([sentence])[0]
	return to_json({'id': id, 'value': sentence, 'is_subjective': int(is_subjective) is 0, 'features': extract([sentence], classifier1.feature_names)})

def clues(request, id, sentence):
	clue_id = int(classifier2.predict([sentence])[0])
	clue = classifier2.target_names[clue_id]

	return to_json({'id': id, 'clue': clue, 'clue_id': clue_id, 'features': extract([sentence], classifier2.feature_names)})

def sentiment(request, clue, id, sentence):
	if clue == 'f':
		classifier = classifier3a
	elif clue == 'h':
		classifier = classifier3b
	elif clue == 'm':
		classifier = classifier3c
	elif clue == 'g':
		classifier = classifier3d

	rating = int(classifier.predict([sentence])[0])

	return to_json({'id': id, 'rating': rating, 'features': extract([sentence], classifier.feature_names)})

def overall(request, functional, humanic, mechanic, general):
	rating = classifier4.predict([[float(functional), float(humanic), float(mechanic), float(general)]])[0]

	return to_json({'rating': int(rating)})
