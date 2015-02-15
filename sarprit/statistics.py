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

def get_clue_ratio():
	reviews = Review.objects.filter(flag=1)
	sentences = [sentence for review in reviews for sentence in review.sentence_set.all()]

	f_sentences = [sentence for sentence in sentences if sentence.clue is 'f']
	h_sentences = [sentence for sentence in sentences if sentence.clue is 'h']
	m_sentences = [sentence for sentence in sentences if sentence.clue is 'm']
	g_sentences = [sentence for sentence in sentences if sentence.clue is 'g']

	print()
	print("F count:", len(f_sentences))
	print("H count:", len(h_sentences))
	print("M count:", len(m_sentences))
	print("G count:", len(g_sentences))

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

					fscore = 0
					hscore = 0
					mscore = 0
					gscore = 0
					sscore = 0

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

						fcount = len(f_sentences) if len(f_sentences) is not 0 else 1
						hcount = len(h_sentences) if len(h_sentences) is not 0 else 1
						mcount = len(m_sentences) if len(m_sentences) is not 0 else 1
						gcount = len(g_sentences) if len(g_sentences) is not 0 else 1

						fscore += sum([
							sentence.rating for sentence in f_sentences
						])/fcount
						hscore += sum([
							sentence.rating for sentence in h_sentences
						])/hcount
						mscore += sum([
							sentence.rating for sentence in m_sentences
						])/mcount
						gscore += sum([
							sentence.rating for sentence in g_sentences
						])/gcount

						sscore += review.overall_sentiment

					print()
					print("%s%s%s%s"%(
						"F" if f is 1 else "",
						"H" if h is 1 else "",
						"M" if m is 1 else "",
						"G" if g is 1 else "",
						))
					print(
						"Original:   %8sf + %8sh + %8sm + %8sg = %8s" % (
						 	"%6.2f"%fscore,
						 	"%6.2f"%hscore,
						 	"%6.2f"%mscore,
						 	"%6.2f"%gscore,
						 	"%6.2f"%sscore
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
						"Impact:     %8sf + %8sh + %8sm + %8sg" % (
						 	"%2.2f"%(fimpact/((clues_count-1) or 1) if f is 1 else 0),
						 	"%2.2f"%(himpact/((clues_count-1) or 1) if h is 1 else 0),
						 	"%2.2f"%(mimpact/((clues_count-1) or 1) if m is 1 else 0),
						 	"%2.2f"%(gimpact/((clues_count-1) or 1) if g is 1 else 0)
						 )
					)

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
