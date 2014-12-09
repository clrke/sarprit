from django.shortcuts import render
from sarprit.shortcuts import to_json
from sarprit.examples import classifier1, classifier2, classifier3a, classifier3b, classifier3c, classifier3d, classifier4

def subjectivity(request, id, sentence):
	is_subjective = classifier1.predict([sentence])[0]
	return to_json({'id': id, 'value': sentence, 'is_subjective': int(is_subjective) is 0})

def clues(request, id, sentence):
	clue_id = int(classifier2.predict([sentence])[0])
	clue = classifier2.target_names[clue_id]

	return to_json({'id': id, 'clue': clue, 'clue_id': clue_id})

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

	return to_json({'id': id, 'rating': rating})

def overall(request, functional, humanic, mechanic, general):
	rating = classifier4.predict([[float(functional), float(humanic), float(mechanic), float(general)]])[0]

	return to_json({'rating': int(rating)})
