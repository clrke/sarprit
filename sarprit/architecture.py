import re
from sarprit.examples import classifier1, classifier2, classifier3a, classifier3b, classifier3c, classifier3d, classifier4
from survey.models import Review

def is_smiley(word):
	hats, eyes, noses, mouths = r"O30o<\|", r":;8BX=<o\.", r"-~'^_", r"\)\(\/\\\|3DPO0\$\*\."
	pattern = "[%s]*[%s][%s]?[%s]+" % tuple(map(re.escape, [hats, eyes, noses, mouths]))

	return re.match(pattern, word) != None

def get_conjunctions():
	conjunctions = []
	for review in Review.objects.all():
		prev_sentence_ended = True
		for sentence in review.sentence_set.all():
			sentence = sentence.sentence.strip()

			if not prev_sentence_ended and sentence[0] != '#' and sentence[0] != '@':
				if len(sentence.split()) != 1 and sentence.split()[0] not in conjunctions:
					conjunctions.append(sentence.split()[0])

			if sentence[0] == '#' or sentence[0] == '@' or sentence[-1] == '.' or sentence[-1] == '!' or sentence[-1] == '?' or is_smiley(sentence.split()[-1]):
				prev_sentence_ended = True
			else:
				prev_sentence_ended = False

	return conjunctions

def phrase_split(sentence):
	phrase_parts = re.split('(%s)'%'|'.join(get_conjunctions()), sentence)

	phrases = [phrase_parts[0]]

	for i in range(len(phrase_parts) // 2):
		phrases.extend(["%s%s" % (phrase_parts[1+i*2], phrase_parts[2+i*2])])

	return phrases

def normalize_hashtag(hashtag):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', hashtag)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)

def sentence_split(review):
	phrases = [phrase[0] for phrase in [phrase_split(s[0]) for s in re.findall(r'(([@#][\w]+ *)|([^\.!\?@#]*[\.!\?]* *))', review)]]

	sentences = []
	for i in range(len(phrases)):
		if phrases[i] != '':
			sentences.append(phrases[i])

	return sentences

def classify(review):
	# sentence splitting
	sentences = sentence_split(review)

	# normalize hashtags
	sentences = [normalize_hashtag(sentences[i]) if sentences[i][0] == '#' else sentences[i] for i in range(len(sentences))]

	# subjectivity classification
	subjectivity = classifier1.predict(sentences)

	# remove objective sentences
	sentences = [sentences[i] for i in range(len(subjectivity)) if subjectivity[i] == 0]

	# if all are objective sentences
	if len(sentences) is 0:
		return 3

	# clues classification
	clues = classifier2.predict(sentences)

	# seperate reviews by clue
	f_sentences = [sentences[i] for i in range(len(clues)) if clues[i] == 0]
	h_sentences = [sentences[i] for i in range(len(clues)) if clues[i] == 1]
	m_sentences = [sentences[i] for i in range(len(clues)) if clues[i] == 2]
	g_sentences = [sentences[i] for i in range(len(clues)) if clues[i] == 3]

	# sentiment analysis per clue
	f_sentiments = [] if len(f_sentences) == 0 else classifier3a.predict(f_sentences)
	h_sentiments = [] if len(h_sentences) == 0 else classifier3b.predict(h_sentences)
	m_sentiments = [] if len(m_sentences) == 0 else classifier3c.predict(m_sentences)
	g_sentiments = [] if len(g_sentences) == 0 else classifier3d.predict(g_sentences)

	# get type of SVM to use
	f = 0 if len(f_sentiments) == 0 else 1
	h = 0 if len(h_sentiments) == 0 else 1
	m = 0 if len(m_sentiments) == 0 else 1
	g = 0 if len(g_sentiments) == 0 else 1

	# get overall sentiment analysis of each
	overall_f = 0 if len(f_sentences) == 0 else sum(f_sentiments)/len(f_sentences)
	overall_h = 0 if len(h_sentences) == 0 else sum(h_sentiments)/len(h_sentences)
	overall_m = 0 if len(m_sentences) == 0 else sum(m_sentiments)/len(m_sentences)
	overall_g = 0 if len(g_sentences) == 0 else sum(g_sentiments)/len(g_sentences)

	# overall sentiment analysis
	overall_sentiment = classifier4[f][h][m][g].predict([[overall_f, overall_h, overall_m, overall_g]])

	return overall_sentiment[0]

