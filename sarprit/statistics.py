from survey.models import Review
from .architecture import classify, classify_without_clues
from sarprit.shortcuts import normalize_sentiment

def get_accuracy(without_clues = False):
	reviews = Review.objects.filter(flag=2)

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
