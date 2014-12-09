from nltk.tokenize import TreebankWordTokenizer

def get_unigrams(sentence):
	return [unigram.lower() for unigram in TreebankWordTokenizer().tokenize(sentence)]

def get_all_unigrams(setences):
	all_unigrams = []

	for sentence in setences:
		for token in get_unigrams(sentence):
			if token not in all_unigrams:
				all_unigrams.append(token)

	return all_unigrams

def get_features(sentence):
	features = get_unigrams(sentence)

	return features

def get_all_features(sentences):
	all_features = get_all_unigrams(sentences)

	return all_features

def extract(sentences, feature_names=None):
	if feature_names is None:
		feature_names = get_all_features(sentences)

	data = []

	for sentence in sentences:
		features = get_features(sentence)
		data.append([features.count(feature) for feature in feature_names])

	return feature_names, data
