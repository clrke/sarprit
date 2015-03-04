from django.shortcuts import render
from django.http import JsonResponse
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

def preprocess(request, review):
	from sarprit.architecture import preprocess
	return JsonResponse(preprocess(review), safe=False)

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

def presentation(request):
	from sarprit.architecture import classify, classify_without_clues
	from survey.models import Review

	reviews = []

	review_count = 0
	classify1_ok_count = 0
	classify2_ok_count = 0

	for review in Review.objects.filter(flag=2):
		review_string = review.raw_string()

		review_count += 1

		classify1 = classify(review_string)
		classify2 = classify_without_clues(review_string)

		normalized_sentiment1 = normalize_sentiment(review.overall_sentiment)
		normalized_sentiment2 = normalize_sentiment(classify1[0])
		normalized_sentiment3 = normalize_sentiment(classify2[0])

		reviews.append((
			review.__str__(),
			normalized_sentiment1,
			normalized_sentiment2,
			normalized_sentiment3
		))

		if normalized_sentiment1 == normalized_sentiment2:
			classify1_ok_count += 1
		if normalized_sentiment1 == normalized_sentiment3:
			classify2_ok_count += 1


	return render(request, 'classifiers/presentation.html',
		{
			'reviews': reviews,
			'review_count': review_count,
			'classify1_ok_count': classify1_ok_count,
			'classify2_ok_count': classify2_ok_count,
		}
	)

def presentation1(request):
	from sarprit.architecture import classify, classify_without_clues

	from survey.models import Review

	table1 = [[[] for column in range(3)] for row in range(3)]
	table2 = [[[] for column in range(3)] for row in range(3)]

	reviews = Review.objects.filter(flag=2)

	for review in reviews:
		review_string = review.raw_string()

		classify1 = classify(review_string)
		classify2 = classify_without_clues(review_string)

		normal1 = normalize_sentiment(review.overall_sentiment)
		normal2 = normalize_sentiment(classify1[0])
		normal3 = normalize_sentiment(classify2[0])

		table1[2-normal2][2-normal1].append(review_string)
		table2[2-normal3][2-normal1].append(review_string)

	return render(request, 'classifiers/presentation1.html',
		{
			'tables': [
				{
					'name': 'With Clues',
					'data': table1,
					'titles': ['Positive', 'Neutral', 'Negative'],
					'colors': ['green', 'grey', 'red']
				},
				{
					'name': 'Without Clues',
					'data': table2,
					'titles': ['Positive', 'Neutral', 'Negative'],
					'colors': ['green', 'grey', 'red']
				}
			],
		})

def presentation2(request):
	from survey.models import Review
	from sarprit.shortcuts import normalize_sentiment

	reviews = Review.objects.filter(flag=1)
	sentences = [sentence for review in reviews for sentence in review.sentence_set.all()]


	table1 = [[[] for column in range(2)] for row in range(1)]
	table2 = [[[] for column in range(3)] for row in range(4)]
	table3 = [[[] for column in range(3)] for row in range(16)]

	subjective_sentences = [sentence for sentence in sentences if sentence.subjective is True]
	objective_sentences = [sentence for sentence in sentences if sentence.subjective is False]

	table1[0][0] = [sentence.sentence for sentence in subjective_sentences]
	table1[0][1] = [sentence.sentence for sentence in objective_sentences]

	for sentence in sentences:
		table2[sentence.int_clue()][2-normalize_sentiment(sentence.rating)].append(sentence.sentence)

	sorted_reviews = [[[[[], []],[[], []]],[[[], []],[[], []]]],[[[[], []],[[], []]],[[[], []],[[], []]]]]

	for review in reviews:
		f=1 if review.sentence_set.filter(clue='f').count() > 0 else 0
		h=1 if review.sentence_set.filter(clue='h').count() > 0 else 0
		m=1 if review.sentence_set.filter(clue='m').count() > 0 else 0
		g=1 if review.sentence_set.filter(clue='g').count() > 0 else 0

		sorted_reviews[f][h][m][g].append(review)

	overall_sentiment_analyzers = []

	for g in range(2):
		for m in range(2):
			for h in range(2):
				for f in range(2):
					reviews = sorted_reviews[f][h][m][g]

					overall_sentiment_analyzers.append("%s%s%s%s"%(
						"F" if f == 1 else "",
						"H" if h == 1 else "",
						"M" if m == 1 else "",
						"G" if g == 1 else ""
					))

					t = g*8+m*4+h*2+f

					for review in reviews:
						normal = normalize_sentiment(review.overall_sentiment)
						table3[t][2-normal].append(review.raw_string())


	return render(request, 'classifiers/presentation2.html',
		{
			'tables': [
				{
					'name': 'Subjective : Objective',
					'data': table1,
					'titlesX': ['Subjective', 'Objective'],
					'titlesY': ['Values'],
					'colorsX': ['green', 'grey'],
					'colorsY': ['black']
				},
				{
					'name': 'Clues',
					'data': table2,
					'titlesX': ['Positive', 'Neutral', 'Negative'],
					'titlesY': ['Functional', 'Humanic', 'Mechanic', 'General'],
					'colorsX': ['green', 'grey', 'red'],
					'colorsY': ['blue', 'orange', 'red', 'green']
				},
				{
					'name': 'Overall Sentiment Analyzers',
					'data': table3,
					'titlesX': ['Positive', 'Neutral', 'Negative'],
					'titlesY': overall_sentiment_analyzers,
					'colorsX': ['green', 'grey', 'red'],
					'colorsY': ['black' for i in range(16)]
				},
			]
		})

def presentation3(request):
	from sarprit.examples import classifier1
	from sarprit.examples import classifier2
	from sarprit.examples import classifier3a
	from sarprit.examples import classifier3b
	from sarprit.examples import classifier3c
	from sarprit.examples import classifier3d
	from sarprit.examples import classifier3e
	from sarprit.examples import classifier4

	from survey.models import Review

	table1 = [[[] for column in range(2)] for row in range(2)]
	table2 = [[[] for column in range(4)] for row in range(4)]
	table3a = [[[] for column in range(3)] for row in range(3)]
	table3b = [[[] for column in range(3)] for row in range(3)]
	table3c = [[[] for column in range(3)] for row in range(3)]
	table3d = [[[] for column in range(3)] for row in range(3)]

	reviews = Review.objects.filter(flag=2)
	sentences = [sentence for review in reviews for sentence in review.sentence_set.all()]

	for sentence in sentences:
		sentence_string = sentence.sentence

		subjective1 = classifier1.predict([sentence.sentence])[0]
		subjective2 = 0 if sentence.subjective else 1

		table1[subjective1][subjective2].append(sentence.sentence)

		if sentence.subjective:
			clue1 = classifier2.predict([sentence.sentence])[0]
			clue2 = sentence.int_clue()

			table2[clue1][clue2].append(sentence.sentence)

			if sentence.clue == 'f':
				classifier = classifier3a
				table = table3a
			elif sentence.clue == 'h':
				classifier = classifier3b
				table = table3b
			elif sentence.clue == 'm':
				classifier = classifier3c
				table = table3c
			elif sentence.clue == 'g':
				classifier = classifier3d
				table = table3d

			sentiment1 = classifier.predict([sentence.sentence])[0]
			sentiment2 = sentence.rating

			normal1 = normalize_sentiment(int(sentiment1))
			normal2 = normalize_sentiment(sentiment2)

			table[2-normal1][2-normal2].append(sentence.sentence)

	return render(request, 'classifiers/presentation1.html',
		{
			'tables': [
				{
					'name': 'Subjectivity Classifier',
					'data': table1,
					'titles': ['Subjective', 'Objective'],
					'colors': ['green', 'grey']
				},
				{
					'name': 'Clues Classifier',
					'data': table2,
					'titles': ['Functional', 'Humanic', 'Mechanic', 'General'],
					'colors': ['blue', 'orange', 'red', 'green']
				},
				{
					'name': 'Functional Sentiment Analyzer',
					'data': table3a,
					'titles': ['Positive', 'Neutral', 'Negative'],
					'colors': ['green', 'grey', 'red']
				},
				{
					'name': 'Humanic Sentiment Analyzer',
					'data': table3b,
					'titles': ['Positive', 'Neutral', 'Negative'],
					'colors': ['green', 'grey', 'red']
				},
				{
					'name': 'Mechanic Sentiment Analyzer',
					'data': table3c,
					'titles': ['Positive', 'Neutral', 'Negative'],
					'colors': ['green', 'grey', 'red']
				},
				{
					'name': 'General Sentiment Analyzer',
					'data': table3d,
					'titles': ['Positive', 'Neutral', 'Negative'],
					'colors': ['green', 'grey', 'red']
				}
			]
		})
