from survey.models import Review
from .architecture import classify
from sarprit.shortcuts import normalize_sentiment

def get_accuracy():
	reviews = Review.objects.all()

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

	print("Precision (Positive):", pp)
	print("Recall (Positive):", rp)
	print("F1-score (Positive):", f1p)
	print()

	print("Precision (Neutral):", pe)
	print("Recall (Neutral):", re)
	print("F1-score (Neutral):", f1e)
	print()

	print("Precision (Negative):", pn)
	print("Recall (Negative):", rn)
	print("F1-score (Negative):", f1n)
	print()
