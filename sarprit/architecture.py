import re
from sarprit.examples import classifier1, classifier2, classifier3a, classifier3b, classifier3c, classifier3d, classifier4

def sentence_split(review):
	return [s[0] for s in re.findall(r'(([@#][\w^#]+ *)|([^\.!\?]*[\.!\?]* *))', review)]

def classify(review):
	# sentence splitting
	sentences = sentence_split(review)

	# subjectivity classification
	subjectivity = classifier1.predict(sentences)

	# remove objective sentences
	sentences = [sentences[i] for i in range(len(subjectivity)) if subjectivity[i] == 0]

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
