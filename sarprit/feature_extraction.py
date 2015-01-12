from nltk.tokenize import TreebankWordTokenizer
from numpy import mean, argsort
import re

def get_unigrams(sentence):
	return [unigram for unigram in TreebankWordTokenizer().tokenize(sentence)]

def get_all_unigrams(setences):
	all_unigrams = []

	for sentence in setences:
		for token in get_unigrams(sentence):
			if token.lower() not in [unigram.lower() for unigram in all_unigrams]:
				all_unigrams.append(token)

	return all_unigrams

def get_rootword(word):
	word = word.lower()

	rootword = re.findall(r'^nakaka(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^makaka(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^naka(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^maka(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^pag(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^ang(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^ma(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^an(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^napaka(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^(\w+)ng', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^pinaka(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^an(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^ka(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^am(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^(\w*)um(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^(\w*)in(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^ni(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^nan(\w+)', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	rootword = re.findall(r'^(\w+)an', word)
	if len(rootword) > 0: return ''.join(syllable for syllable in rootword[0])

	return word

def get_features(sentence):
	features = get_unigrams(sentence)

	additional_features = []
	for feature in features:
		rootword = get_rootword(feature)
		if rootword != feature:
			additional_features.append(rootword)

	for feature in additional_features:
		features.append(feature)

	return features

def get_all_features(sentences):
	all_features = get_all_unigrams(sentences)

	return all_features

def get_capitalization_points(feature):
	capitalization_points = 0
	for c in feature:
		if c.isupper():
			capitalization_points += 1

	return 1 + capitalization_points / len(feature)

def get_feature_points(features, feature):
	feature_points = 0
	for f in features:
		if f.lower() == feature.lower():
			feature_points += get_capitalization_points(f)

	return feature_points

def extract(sentences, feature_names=None):
	if feature_names is None:
		feature_names = get_all_features(sentences)

	data = []

	for sentence in sentences:
		features = get_features(sentence)
		data.append([get_feature_points(features, feature) for feature in feature_names])

	return feature_names, data

def get_mutual_information(all_features, feature_names, targets, overall_sentiment=False):
	mutual_information = []
	for target in range(max(targets)+1):
		if overall_sentiment:
			mi_values = [mean([all_features[j][i] for j in range(len(all_features)) if targets[j] == target]) for i in range(len(all_features[0]))]
		else:
			mi_values = [mean([(all_features[j][i] if targets[j] == target else 0) for j in range(len(all_features))]) for i in range(len(all_features[0]))]
		mi = []

		if overall_sentiment:
			for i in range(len(mi_values)):
				mi.append((feature_names[i], mi_values[i]))
		else:
			for i in argsort(mi_values)[::-1]:
				mi.append((feature_names[i], mi_values[i]))

		mutual_information.append(mi)

	return mutual_information
