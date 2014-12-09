from django.shortcuts import render
from sarprit.shortcuts import to_json
from sarprit.examples import classifier1, classifier2, classifier3a, classifier3b, classifier3c, classifier3d, classifier4

def subjectivity(request, sentence, id):
	is_subjective = classifier1.predict([sentence])[0]
	return to_json({'id': id, 'value': sentence, 'is_subjective': int(is_subjective) is 0})
