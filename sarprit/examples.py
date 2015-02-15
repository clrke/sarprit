from survey.models import Sentence, Review
import os

def subjective_sentences():
	return [
		"Ang sarap ng pagkain!",
		"Nakakatuwa sila magserve ng pagkain.",
		"Hindi ako naiintindihan ng cashier.",
		"Ang sarap-sarap ng sisig nila at mura pa, paborito na ito ng tropa ko!",
		"#panaloSiKuyangWaiter",
		"Sobrang baho sa lugar nila!",
	]

def objective_sentences():
	return [
		"Ang spaghetti ay isang pagkaing puro pasta.",
		"You are what you eat.",
		"Ang mga kinakain mo ay ang kung sino ikaw",
		"Kumakain kami ngayon sa McDo.",
		"Here at SM Sta Mesa Food Court!",
		"Gagala ba tayo ngayon?",
	]

if os.environ['SCIPY_INSTALLED'] == 'yes':
	from classifiers import classifiers
	def subjectivity_classifier():
		ss = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(subjective=True)
		]

		os = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(subjective=False)
		]

		training_data = ss + os
		target = [0] * len(ss) + [1] * len(os)

		return classifiers.SubjectivityClassifier().fit(training_data, target)


	def clues_classifier():
		f = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(clue='f')
		]

		h = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(clue='h')
		]

		m = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(clue='m')
		]

		g = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(clue='g')
		]

		training_data = f + h + m + g
		target = [0] * len(f) + [1] * len(h) + [2] * len(m) + [3] * len(g)

		return classifiers.CluesClassifier().fit(training_data, target)

	def sentiment_classifier(clue):
		s1 = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(rating=1, clue=clue)
		]
		s2 = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(rating=2, clue=clue)
		]
		s3 = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(rating=3, clue=clue)
		]
		s4 = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(rating=4, clue=clue)
		]
		s5 = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(rating=5, clue=clue)
		]

		training_data = s1 + s2 + s3 + s4 + s5
		target = [1] * len(s1) + [2] * len(s2) + [3] * len(s3) + [4] * len(s4) + [5] * len(s5)

		return classifiers.SentimentClassifier().fit(training_data, target)

	def sentiment_classifier2():
		s1 = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(rating=1)
		]
		s2 = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(rating=2)
		]
		s3 = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(rating=3)
		]
		s4 = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(rating=4)
		]
		s5 = [
			sentence.sentence for review in
				Review.objects.filter(flag=1) for sentence in
					review.sentence_set.filter(rating=5)
		]
		training_data = s1 + s2 + s3 + s4 + s5
		target = [1] * len(s1) + [2] * len(s2) + [3] * len(s3) + [4] * len(s4) + [5] * len(s5)

		return classifiers.SentimentClassifier().fit(training_data, target)

	def overall_classifier2():
		reviews=Review.objects.all()
		features=[]
		targets=[]
		for review in reviews:
			sentence_count=review.sentence_set.count()
			f=sum([sentence.rating for sentence in review.sentence_set.filter(clue='f')])/sentence_count
			h=sum([sentence.rating for sentence in review.sentence_set.filter(clue='h')])/sentence_count
			m=sum([sentence.rating for sentence in review.sentence_set.filter(clue='m')])/sentence_count
			g=sum([sentence.rating for sentence in review.sentence_set.filter(clue='g')])/sentence_count

			features.append([f,h,m,g])
			targets.append(review.overall_sentiment)

		return classifiers.OverallClassifier().fit(features, targets)

	def overall_classifier():
		reviews=Review.objects.all()

		sorted_reviews = [[[[[], []],[[], []]],[[[], []],[[], []]]],[[[[], []],[[], []]],[[[], []],[[], []]]]]
		overall_classifiers = [[[[[], []],[[], []]],[[[], []],[[], []]]],[[[[], []],[[], []]],[[[], []],[[], []]]]]

		for review in reviews:
			f=1 if review.sentence_set.filter(clue='f').count() > 0 else 0
			h=1 if review.sentence_set.filter(clue='h').count() > 0 else 0
			m=1 if review.sentence_set.filter(clue='m').count() > 0 else 0
			g=1 if review.sentence_set.filter(clue='g').count() > 0 else 0

			sorted_reviews[f][h][m][g].append(review)

		for f in range(2):
			for h in range(2):
				for m in range(2):
					for g in range(2):
						features = []
						targets = []

						for review in sorted_reviews[f][h][m][g]:
							f_sentences = review.sentence_set.filter(clue='f')
							h_sentences = review.sentence_set.filter(clue='h')
							m_sentences = review.sentence_set.filter(clue='m')
							g_sentences = review.sentence_set.filter(clue='g')

							feature_f=0 if f_sentences.count() == 0 else sum([sentence.rating for sentence in f_sentences])/f_sentences.count()
							feature_h=0 if h_sentences.count() == 0 else sum([sentence.rating for sentence in h_sentences])/h_sentences.count()
							feature_m=0 if m_sentences.count() == 0 else sum([sentence.rating for sentence in m_sentences])/m_sentences.count()
							feature_g=0 if g_sentences.count() == 0 else sum([sentence.rating for sentence in g_sentences])/g_sentences.count()

							features.append([feature_f, feature_h, feature_m, feature_g])
							targets.append(review.overall_sentiment)

						try:
							overall_classifiers[f][h][m][g] = classifiers.OverallClassifier().fit(features, targets)
						except:
							print("Fail: ", f, h, m, g)
							overall_classifiers[f][h][m][g] = classifiers.OverallClassifier().fit([[1,1,1,1], [3, 3, 3, 3], [5,5,5,5]], [1,3,5])

		return overall_classifiers

	def classifiers_refresh():
		print('Initializing subjectivity classifier...')
		global classifier1
		classifier1 = subjectivity_classifier()
		print('Initializing clues classifier...')
		global classifier2
		classifier2 = clues_classifier()
		print('Initializing sentiment classifier for functional sentences...')
		global classifier3a
		classifier3a = sentiment_classifier('f')
		print('Initializing sentiment classifier for humanic sentences...')
		global classifier3b
		classifier3b = sentiment_classifier('h')
		print('Initializing sentiment classifier for mechanic sentences...')
		global classifier3c
		classifier3c = sentiment_classifier('m')
		print('Initializing sentiment classifier for general sentences...')
		global classifier3d
		classifier3d = sentiment_classifier('g')
		print('Initializing sentiment classifier for no clue sentences...')
		global classifier3e
		classifier3e = sentiment_classifier2()
		print('Initializing overall sentiment classifier...')
		global classifier4
		classifier4 = overall_classifier()
else:
	def classifiers_refresh():
		print('Classifying is prohibited')

classifier1 = None
classifier2 = None
classifier3a = None
classifier3b = None
classifier3c = None
classifier3d = None
classifier3e = None
classifier4 = None
classifiers_refresh()
