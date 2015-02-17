from survey.models import Review, Sentence
from .architecture import classify, classify_without_clues
from sarprit.shortcuts import normalize_sentiment
from .examples import classifier1, classifier2, classifier3a, classifier3b, classifier3c, classifier3d

def get_subjectivity_classifier_accuracy(sentences):
	print("Accuracy of Subjectivity Classifier:")

	ts = 0
	to = 0
	fs = 0
	fo = 0

	s = 0
	o = 0

	for sentence in sentences:
		subjective = classifier1.predict([sentence.sentence])[0]
		if sentence.subjective:
			s += 1
			if subjective == 0:
				ts += 1
			else:
				fo += 1
		else:
			o += 1
			if subjective == 0:
				fs += 1
			else:
				to += 1

		print(ts, to, fs, fo)

	ps = ts/(ts+fs)
	po = to/(to+fo)

	rs = ts/s
	ro = to/o

	f1s = 2 * ((ps * rs)/(ps + rs))
	f1o = 2 * ((po * ro)/(po + ro))

	print("Subjective:")
	print("\tPrecision:", ps)
	print("\tRecall:   ", rs)
	print("\tF1-score: ", f1s)
	print()

	print("Objective:")
	print("\tPrecision:", po)
	print("\tRecall:   ", ro)
	print("\tF1-score: ", f1o)
	print()

def get_overall_sentiment_classifier_accuracy(reviews, without_clues):
	print("Accuracy of Overall Sentiment Classifier:")

	tp = 0
	te = 0
	tn = 0
	fp = 0
	fe = 0
	fn = 0

	p = 0
	e = 0
	n = 0

	for review in reviews:
		if without_clues:
			sentiment, sentences = classify_without_clues(review.raw_string())
		else:
			sentiment, sentences = classify(review.raw_string())

		sentiment1 = normalize_sentiment(sentiment)
		sentiment2 = normalize_sentiment(review.overall_sentiment)

		if sentiment1 == 0: # negative
			n += 1
			if sentiment2 == 0: # negative
				tn += 1
			elif sentiment2 == 1: # neutral
				fe += 1
			elif sentiment2 == 2: # positive
				fp += 1
		elif sentiment1 == 1: # neutral
			e += 1
			if sentiment2 == 0: # negative
				fn += 1
			elif sentiment2 == 1: # neutral
				te += 1
			elif sentiment2 == 2: # positive
				fp += 1
		elif sentiment1 == 2: # positive
			p += 1
			if sentiment2 == 0: # negative
				fn += 1
			elif sentiment2 == 1: # neutral
				fe += 1
			elif sentiment2 == 2: # positive
				tp += 1

		print(tp, te, tn, fp, fe, fn)

	pp = tp/(tp+fp)
	pe = te/(te+fe)
	pn = tn/(tn+fn)

	rp = tp/p
	re = te/e
	rn = tn/n

	f1p = 2 * ((pp * rp)/(pp + rp))
	f1e = 2 * ((pe * re)/(pe + re))
	f1n = 2 * ((pn * rn)/(pn + rn))

	print("Positive:")
	print("\tPrecision:", pp)
	print("\tRecall:   ", rp)
	print("\tF1-score: ", f1p)
	print()

	print("Neutral:")
	print("\tPrecision:", pe)
	print("\tRecall:   ", re)
	print("\tF1-score: ", f1e)
	print()

	print("Negative:")
	print("\tPrecision:", pn)
	print("\tRecall:   ", rn)
	print("\tF1-score: ", f1n)
	print()

def get_accuracy(without_clues = False):
	reviews = Review.objects.filter(flag=2)
	sentences = [sentence for review in reviews for sentence in review.sentence_set.all()]

	get_subjectivity_classifier_accuracy(sentences)

	get_overall_sentiment_classifier_accuracy(reviews, without_clues)

def get_score(sentences):
	count = len(sentences) or 1
	return sum([sentence.rating for sentence in sentences])/count

def get_clues_impact(f, h, m, g, fscore, hscore, mscore, gscore, sscore):
	fdiff = abs(sscore - fscore) if f is 1 else 0
	hdiff = abs(sscore - hscore) if h is 1 else 0
	mdiff = abs(sscore - mscore) if m is 1 else 0
	gdiff = abs(sscore - gscore) if g is 1 else 0
	diff_sum = (fdiff + hdiff + mdiff + gdiff) or 1

	clues_count = f + h + m + g

	if clues_count > 0:
		fimpact = 1 - fdiff/diff_sum
		himpact = 1 - hdiff/diff_sum
		mimpact = 1 - mdiff/diff_sum
		gimpact = 1 - gdiff/diff_sum
	else:
		fimpact = 0
		himpact = 0
		mimpact = 0
		gimpact = 0

	print(
		"Impact:     %8s    %8s    %8s    %8s  = %8s" % (
		 	"x %2.2f"%(fimpact/((clues_count-1) or 1) if f is 1 else 0),
		 	"x %2.2f"%(himpact/((clues_count-1) or 1) if h is 1 else 0),
		 	"x %2.2f"%(mimpact/((clues_count-1) or 1) if m is 1 else 0),
		 	"x %2.2f"%(gimpact/((clues_count-1) or 1) if g is 1 else 0),
		 	"x 1.00"
		 )
	)

def get_data_ratio():
	reviews = Review.objects.filter(flag=1)
	sentences = [sentence for review in reviews for sentence in review.sentence_set.all()]

	subjective_sentences = [sentence for sentence in sentences if sentence.subjective is True]
	objective_sentences = [sentence for sentence in sentences if sentence.subjective is False]

	print()
	print("Subjective count:", len(subjective_sentences))
	print("Objective count: ", len(objective_sentences))

	f_sentences = [sentence for sentence in sentences if sentence.clue is 'f']
	h_sentences = [sentence for sentence in sentences if sentence.clue is 'h']
	m_sentences = [sentence for sentence in sentences if sentence.clue is 'm']
	g_sentences = [sentence for sentence in sentences if sentence.clue is 'g']

	fp = [sentence for sentence in f_sentences if sentence.rating >  3]
	fe = [sentence for sentence in f_sentences if sentence.rating is 3]
	fn = [sentence for sentence in f_sentences if sentence.rating <  3]

	hp = [sentence for sentence in h_sentences if sentence.rating >  3]
	he = [sentence for sentence in h_sentences if sentence.rating is 3]
	hn = [sentence for sentence in h_sentences if sentence.rating <  3]

	mp = [sentence for sentence in m_sentences if sentence.rating >  3]
	me = [sentence for sentence in m_sentences if sentence.rating is 3]
	mn = [sentence for sentence in m_sentences if sentence.rating <  3]

	gp = [sentence for sentence in g_sentences if sentence.rating >  3]
	ge = [sentence for sentence in g_sentences if sentence.rating is 3]
	gn = [sentence for sentence in g_sentences if sentence.rating <  3]

	print()
	print("F count: %4s | %4s %4s %4s" % (len(f_sentences), len(fp), len(fe), len(fn)))
	print("H count: %4s | %4s %4s %4s" % (len(h_sentences), len(hp), len(he), len(hn)))
	print("M count: %4s | %4s %4s %4s" % (len(m_sentences), len(mp), len(me), len(mn)))
	print("G count: %4s | %4s %4s %4s" % (len(g_sentences), len(gp), len(ge), len(gn)))

	sorted_reviews = [[[[[], []],[[], []]],[[[], []],[[], []]]],[[[[], []],[[], []]],[[[], []],[[], []]]]]

	for review in reviews:
		f=1 if review.sentence_set.filter(clue='f').count() > 0 else 0
		h=1 if review.sentence_set.filter(clue='h').count() > 0 else 0
		m=1 if review.sentence_set.filter(clue='m').count() > 0 else 0
		g=1 if review.sentence_set.filter(clue='g').count() > 0 else 0

		sorted_reviews[f][h][m][g].append(review)

	for g in range(2):
		for m in range(2):
			for h in range(2):
				for f in range(2):
					reviews = sorted_reviews[f][h][m][g]

					reviews_count = len(reviews)

					fscores = []
					hscores = []
					mscores = []
					gscores = []
					sscores = []

					for review in reviews:
						f_sentences = [
							sentence for sentence in review.sentence_set.all() if sentence.clue is 'f'
						]
						h_sentences = [
							sentence for sentence in review.sentence_set.all() if sentence.clue is 'h'
						]
						m_sentences = [
							sentence for sentence in review.sentence_set.all() if sentence.clue is 'm'
						]
						g_sentences = [
							sentence for sentence in review.sentence_set.all() if sentence.clue is 'g'
						]

						fscore = get_score(f_sentences)
						hscore = get_score(h_sentences)
						mscore = get_score(m_sentences)
						gscore = get_score(g_sentences)

						sscore = review.overall_sentiment

						fscores.append(fscore)
						hscores.append(hscore)
						mscores.append(mscore)
						gscores.append(gscore)
						sscores.append(sscore)

					fscore = sum([score for score in fscores])/(reviews_count or 1)
					hscore = sum([score for score in hscores])/(reviews_count or 1)
					mscore = sum([score for score in mscores])/(reviews_count or 1)
					gscore = sum([score for score in gscores])/(reviews_count or 1)
					sscore = sum([score for score in sscores])/(reviews_count or 1)

					print()
					print("%s%s%s%s: %d"%(
						"F" if f is 1 else "",
						"H" if h is 1 else "",
						"M" if m is 1 else "",
						"G" if g is 1 else "",
						reviews_count
						))
					print(
						"Original:   %8sf + %8sh + %8sm + %8sg = %8s" % (
						 	"%6.2f"%(fscore),
						 	"%6.2f"%(hscore),
						 	"%6.2f"%(mscore),
						 	"%6.2f"%(gscore),
						 	"%6.2f"%(sscore)
						 )
					)
					print(
						"Simplified: %8sf + %8sh + %8sm + %8sg = %8s" % (
						 	"%2.2f"%(fscore/sscore),
						 	"%2.2f"%(hscore/sscore),
						 	"%2.2f"%(mscore/sscore),
						 	"%2.2f"%(gscore/sscore),
						 	"%2.2f"%(sscore/sscore)
						 )
					)
					get_clues_impact(f, h, m, g, fscore, hscore, mscore, gscore, sscore)

def randomize_review_flags():
	from random import shuffle

	reviews = list(Review.objects.all().exclude(flag=0))

	print("Shuffling reviews...")
	shuffle(reviews)

	print("Selecting train and test data...")
	length = len(reviews)
	train_reviews = reviews[:int(length*3/4)]
	test_reviews  = reviews[int(length*3/4):]

	print("Train Reviews count:", len(train_reviews))
	print("Test Reviews count: ", len(test_reviews))

	for review in train_reviews:
		review.flag = 1
		review.save()

	for review in test_reviews:
		review.flag = 2
		review.save()

def set_review_flags_to_training():
	for review in Review.objects.all():
		review.flag = 1
		review.save()
