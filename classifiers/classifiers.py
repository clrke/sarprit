from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sarprit import feature_extraction

class SubjectivityClassifier(MultinomialNB):
	def __init__(self):
		super(SubjectivityClassifier, self).__init__()

	def fit(self, training_data, target):
		self.target = target
		self.target_names = ['subjective', 'objective']
		self.feature_names, self.features = feature_extraction.extract(training_data)

		return super(SubjectivityClassifier, self).fit(self.features, self.target)

	def predict(self, predict_data):
		feature_names, features = feature_extraction.extract(predict_data, self.feature_names)

		return super(SubjectivityClassifier, self).predict(features)

	def predict_proba(self, predict_data):
		feature_names, features = feature_extraction.extract(predict_data, self.feature_names)

		return super(SubjectivityClassifier, self).predict_proba(features)

	def score(self, predict_data, target_data, sample_weight=None):
		return super(SubjectivityClassifier, self).score(predict_data, target_data, sample_weight)

class CluesClassifier(MultinomialNB):
	def __init__(self):
		super(CluesClassifier, self).__init__()

	def fit(self, training_data, target):
		self.target = target
		self.target_names = ['Functional', 'Humanic','Mechanic','General']
		self.feature_names, self.features = feature_extraction.extract(training_data)

		return super(CluesClassifier, self).fit(self.features, self.target)

	def predict(self, predict_data):
		feature_names, features = feature_extraction.extract(predict_data, self.feature_names)

		return super(CluesClassifier, self).predict(features)

	def predict_proba(self, predict_data):
		feature_names, features = feature_extraction.extract(predict_data, self.feature_names)

		return super(CluesClassifier, self).predict_proba(features)

	def score(self, predict_data, target_data, sample_weight=None):
		return super(CluesClassifier, self).score(predict_data, target_data, sample_weight)

class SentimentClassifier(MultinomialNB):
	def __init__(self):
		super(SentimentClassifier, self).__init__()

	def fit(self, training_data, target):
		self.target = target
		self.target_names = ['1', '2','3','4','5']
		self.feature_names, self.features = feature_extraction.extract(training_data)

		return super(SentimentClassifier, self).fit(self.features, self.target)

	def predict(self, predict_data):
		feature_names, features = feature_extraction.extract(predict_data, self.feature_names)

		return super(SentimentClassifier, self).predict(features)

	def predict_proba(self, predict_data):
		feature_names, features = feature_extraction.extract(predict_data, self.feature_names)

		return super(SentimentClassifier, self).predict_proba(features)

	def score(self, predict_data, target_data, sample_weight=None):
		return super(SentimentClassifier, self).score(predict_data, target_data, sample_weight)

class OverallClassifier(SVC):
	def __init__(self):
		super(OverallClassifier, self).__init__()

	def fit(self, training_data, target):
		self.feature_names = ['Functional', 'Humanic', 'Mechanic', 'General']
		self.features= training_data
		self.target = target

		return super(OverallClassifier, self).fit(self.features, self.target)

	def predict(self, predict_data):
		return super(OverallClassifier, self).predict(predict_data)

	def predict_proba(self, predict_data):
		return super(OverallClassifier, self).predict_proba(predict_data)

	def score(self, predict_data, target_data, sample_weight=None):
		return super(OverallClassifier, self).score(predict_data, target_data, sample_weight)
