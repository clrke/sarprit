from django.shortcuts import render
from sarprit.shortcuts import to_json, normalize_sentiment
from sarprit.feature_extraction import extract

def home(request):
	from sarprit.examples import classifier1, classifier2, classifier3a, classifier3b, classifier3c, classifier3d, classifier4
	from sarprit.feature_extraction import get_mutual_information

	mi_max = 12
	mutual_information = {
		'subjectivity' : 	[mi[:mi_max] for mi in get_mutual_information(classifier1.features, classifier1.feature_names, classifier1.target)],
		'clue' : 			[mi[:mi_max] for mi in get_mutual_information(classifier2.features, classifier2.feature_names, classifier2.target)],
		'sentiment1' : 		[mi[:mi_max] for mi in get_mutual_information(classifier3a.features, classifier3a.feature_names, [normalize_sentiment(target) for target in classifier3a.target])],
		'sentiment2' : 		[mi[:mi_max] for mi in get_mutual_information(classifier3b.features, classifier3b.feature_names, [normalize_sentiment(target) for target in classifier3b.target])],
		'sentiment3' : 		[mi[:mi_max] for mi in get_mutual_information(classifier3c.features, classifier3c.feature_names, [normalize_sentiment(target) for target in classifier3c.target])],
		'sentiment4' : 		[mi[:mi_max] for mi in get_mutual_information(classifier3d.features, classifier3d.feature_names, [normalize_sentiment(target) for target in classifier3d.target])],
	}

	for g in range(2):
		for m in range(2):
			for h in range(2):
				for f in range(2):
					mutual_information['overall'+str(f)+str(h)+str(m)+str(g)] = [mi[:mi_max] for mi in get_mutual_information(classifier4[f][h][m][g].features, classifier4[f][h][m][g].feature_names, [normalize_sentiment(target) for target in classifier4[f][h][m][g].target], True)]

	mutual_information['table_data'] = [
		(
			mutual_information['subjectivity'][0][i] if 0 < len(mutual_information['subjectivity']) else None,
			mutual_information['subjectivity'][1][i] if 1 < len(mutual_information['subjectivity']) else None,
			mutual_information['clue'][0][i] if 0 < len(mutual_information['clue']) else None,
			mutual_information['clue'][1][i] if 1 < len(mutual_information['clue']) else None,
			mutual_information['clue'][2][i] if 2 < len(mutual_information['clue']) else None,
			mutual_information['clue'][3][i] if 3 < len(mutual_information['clue']) else None,
			mutual_information['sentiment1'][0][i] if 0 < len(mutual_information['sentiment1']) else None,
			mutual_information['sentiment1'][1][i] if 1 < len(mutual_information['sentiment1']) else None,
			mutual_information['sentiment1'][2][i] if 2 < len(mutual_information['sentiment1']) else None,
			mutual_information['sentiment2'][0][i] if 0 < len(mutual_information['sentiment2']) else None,
			mutual_information['sentiment2'][1][i] if 1 < len(mutual_information['sentiment2']) else None,
			mutual_information['sentiment2'][2][i] if 2 < len(mutual_information['sentiment2']) else None,
			mutual_information['sentiment3'][0][i] if 0 < len(mutual_information['sentiment3']) else None,
			mutual_information['sentiment3'][1][i] if 1 < len(mutual_information['sentiment3']) else None,
			mutual_information['sentiment3'][2][i] if 2 < len(mutual_information['sentiment3']) else None,
			mutual_information['sentiment4'][0][i] if 0 < len(mutual_information['sentiment4']) else None,
			mutual_information['sentiment4'][1][i] if 1 < len(mutual_information['sentiment4']) else None,
			mutual_information['sentiment4'][2][i] if 2 < len(mutual_information['sentiment4']) else None,
			mutual_information['overall1000'][0][i] if i < 4 and 0 < len(mutual_information['overall1000']) else None,
			mutual_information['overall1000'][1][i] if i < 4 and 1 < len(mutual_information['overall1000']) else None,
			mutual_information['overall1000'][2][i] if i < 4 and 2 < len(mutual_information['overall1000']) else None,
			mutual_information['overall0100'][0][i] if i < 4 and 0 < len(mutual_information['overall0100']) else None,
			mutual_information['overall0100'][1][i] if i < 4 and 1 < len(mutual_information['overall0100']) else None,
			mutual_information['overall0100'][2][i] if i < 4 and 2 < len(mutual_information['overall0100']) else None,
			mutual_information['overall1100'][0][i] if i < 4 and 0 < len(mutual_information['overall1100']) else None,
			mutual_information['overall1100'][1][i] if i < 4 and 1 < len(mutual_information['overall1100']) else None,
			mutual_information['overall1100'][2][i] if i < 4 and 2 < len(mutual_information['overall1100']) else None,
			mutual_information['overall0010'][0][i] if i < 4 and 0 < len(mutual_information['overall0010']) else None,
			mutual_information['overall0010'][1][i] if i < 4 and 1 < len(mutual_information['overall0010']) else None,
			mutual_information['overall0010'][2][i] if i < 4 and 2 < len(mutual_information['overall0010']) else None,
			mutual_information['overall1010'][0][i] if i < 4 and 0 < len(mutual_information['overall1010']) else None,
			mutual_information['overall1010'][1][i] if i < 4 and 1 < len(mutual_information['overall1010']) else None,
			mutual_information['overall1010'][2][i] if i < 4 and 2 < len(mutual_information['overall1010']) else None,
			mutual_information['overall0110'][0][i] if i < 4 and 0 < len(mutual_information['overall0110']) else None,
			mutual_information['overall0110'][1][i] if i < 4 and 1 < len(mutual_information['overall0110']) else None,
			mutual_information['overall0110'][2][i] if i < 4 and 2 < len(mutual_information['overall0110']) else None,
			mutual_information['overall1110'][0][i] if i < 4 and 0 < len(mutual_information['overall1110']) else None,
			mutual_information['overall1110'][1][i] if i < 4 and 1 < len(mutual_information['overall1110']) else None,
			mutual_information['overall1110'][2][i] if i < 4 and 2 < len(mutual_information['overall1110']) else None,
			mutual_information['overall0001'][0][i] if i < 4 and 0 < len(mutual_information['overall0001']) else None,
			mutual_information['overall0001'][1][i] if i < 4 and 1 < len(mutual_information['overall0001']) else None,
			mutual_information['overall0001'][2][i] if i < 4 and 2 < len(mutual_information['overall0001']) else None,
			mutual_information['overall1001'][0][i] if i < 4 and 0 < len(mutual_information['overall1001']) else None,
			mutual_information['overall1001'][1][i] if i < 4 and 1 < len(mutual_information['overall1001']) else None,
			mutual_information['overall1001'][2][i] if i < 4 and 2 < len(mutual_information['overall1001']) else None,
			mutual_information['overall0101'][0][i] if i < 4 and 0 < len(mutual_information['overall0101']) else None,
			mutual_information['overall0101'][1][i] if i < 4 and 1 < len(mutual_information['overall0101']) else None,
			mutual_information['overall0101'][2][i] if i < 4 and 2 < len(mutual_information['overall0101']) else None,
			mutual_information['overall1101'][0][i] if i < 4 and 0 < len(mutual_information['overall1101']) else None,
			mutual_information['overall1101'][1][i] if i < 4 and 1 < len(mutual_information['overall1101']) else None,
			mutual_information['overall1101'][2][i] if i < 4 and 2 < len(mutual_information['overall1101']) else None,
			mutual_information['overall0011'][0][i] if i < 4 and 0 < len(mutual_information['overall0011']) else None,
			mutual_information['overall0011'][1][i] if i < 4 and 1 < len(mutual_information['overall0011']) else None,
			mutual_information['overall0011'][2][i] if i < 4 and 2 < len(mutual_information['overall0011']) else None,
			mutual_information['overall1011'][0][i] if i < 4 and 0 < len(mutual_information['overall1011']) else None,
			mutual_information['overall1011'][1][i] if i < 4 and 1 < len(mutual_information['overall1011']) else None,
			mutual_information['overall1011'][2][i] if i < 4 and 2 < len(mutual_information['overall1011']) else None,
			mutual_information['overall0111'][0][i] if i < 4 and 0 < len(mutual_information['overall0111']) else None,
			mutual_information['overall0111'][1][i] if i < 4 and 1 < len(mutual_information['overall0111']) else None,
			mutual_information['overall0111'][2][i] if i < 4 and 2 < len(mutual_information['overall0111']) else None,
			mutual_information['overall1111'][0][i] if i < 4 and 0 < len(mutual_information['overall1111']) else None,
			mutual_information['overall1111'][1][i] if i < 4 and 1 < len(mutual_information['overall1111']) else None,
			mutual_information['overall1111'][2][i] if i < 4 and 2 < len(mutual_information['overall1111']) else None,
		)
		for i in range(mi_max)
	]

	return render(request, 'classifiers/index.html',
		{
			'mutual_information': mutual_information,
			'classifier1' : { 'feature_names': classifier1.feature_names, 'data': [(classifier1.features[i], classifier1.target[i]) for i in range(len(classifier1.features))] },
			'classifier2' : { 'feature_names': classifier2.feature_names, 'data': [(classifier2.features[i], classifier2.target[i]) for i in range(len(classifier2.features))] },
			'classifier3a' : { 'feature_names': classifier3a.feature_names, 'data': [(classifier3a.features[i], classifier3a.target[i]) for i in range(len(classifier3a.features))] },
			'classifier3b' : { 'feature_names': classifier3b.feature_names, 'data': [(classifier3b.features[i], classifier3b.target[i]) for i in range(len(classifier3b.features))] },
			'classifier3c' : { 'feature_names': classifier3c.feature_names, 'data': [(classifier3c.features[i], classifier3c.target[i]) for i in range(len(classifier3c.features))] },
			'classifier3d' : { 'feature_names': classifier3d.feature_names, 'data': [(classifier3d.features[i], classifier3d.target[i]) for i in range(len(classifier3d.features))] },
			'classifier4' :  { 'feature_names': classifier4[1][0][0][0].feature_names, 'data': sorted([(classifier4[1][0][0][0].features[i], classifier4[1][0][0][0].target[i]) for i in range(len(classifier4[1][0][0][0].features))], key=lambda x: x[1]) },
		})

def subjectivity(request, id, sentence):
	from sarprit.examples import classifier1, classifier2, classifier3a, classifier3b, classifier3c, classifier3d, classifier4
	is_subjective = classifier1.predict([sentence])[0]
	return to_json({'id': id, 'value': sentence, 'is_subjective': int(is_subjective) is 0, 'features': extract([sentence], classifier1.feature_names)})

def clues(request, id, sentence):
	from sarprit.examples import classifier1, classifier2, classifier3a, classifier3b, classifier3c, classifier3d, classifier4
	clue_id = int(classifier2.predict([sentence])[0])
	clue = classifier2.target_names[clue_id]

	return to_json({'id': id, 'clue': clue, 'clue_id': clue_id, 'features': extract([sentence], classifier2.feature_names)})

def sentiment(request, clue, id, sentence):
	from sarprit.examples import classifier1, classifier2, classifier3a, classifier3b, classifier3c, classifier3d, classifier4
	if clue == 'f':
		classifier = classifier3a
	elif clue == 'h':
		classifier = classifier3b
	elif clue == 'm':
		classifier = classifier3c
	elif clue == 'g':
		classifier = classifier3d
	elif clue == 'n':
		from sarprit.examples import classifier3e
		classifier = classifier3e

	rating = int(classifier.predict([sentence])[0])

	return to_json({'id': id, 'rating': rating, 'features': extract([sentence], classifier.feature_names)})

def overall(request, functional, humanic, mechanic, general):
	from sarprit.examples import classifier1, classifier2, classifier3a, classifier3b, classifier3c, classifier3d, classifier4

	f=0 if functional == '0' else 1
	h=0 if humanic == '0' else 1
	m=0 if mechanic == '0' else 1
	g=0 if general == '0' else 1

	rating = classifier4[f][h][m][g].predict([[functional, humanic, mechanic, general]])[0]

	return to_json({'rating': int(rating)})
