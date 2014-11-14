from sklearn.naive_bayes import MultinomialNB
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