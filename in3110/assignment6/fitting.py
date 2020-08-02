import sklearn
sklearn.__version__
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import data
from sklearn.metrics import accuracy_score


def fit(training_set_X, features, model):
	"""
	This function fits training sets based on the training set, it's features and the selected model

	Args:
		training_set_X(Dataframe): Training set
		features(['']): features to fit trainig set with
		model(int): 1 for K Neighbors Classifier, 2 for Quadratic Discriminant Analysis

	Returns:
		model.fit()(fitted clasifier): fitted clasifier for either knn or qda
	"""

	knn = KNeighborsClassifier()
	qda = QuadraticDiscriminantAnalysis()

	target = training_set_X.pop('diabetes')
	train = training_set_X[features]

	if model == 1 :
		return knn.fit(train, target)
	elif model == 2 :
		return qda.fit(train, target)


def Test():
	"""
		This function runs two models and checks their accuracy

		Args:
			None
		Returns:
			None
	"""

	training_set = data.get_training_set().copy()
	validation_set = data.get_validation_set().copy()
	features = ['age','pressure',  'triceps','mass']
	fitted  =  fit(training_set, features, 1)
	pred_fitted = fitted.predict(validation_set[features])
	fit_score = accuracy_score(validation_set['diabetes'], pred_fitted)

	print("KNeighborsClassifier with features: age, pressure, triceps, mass" )
	print("Score: ""{0:.2f}".format(fit_score*100) + "%")

	training_set = data.get_training_set().copy()
	validation_set = data.get_validation_set().copy()
	features = ['age','pressure',  'triceps','mass']
	fitted  =  fit(training_set, features, 2)
	pred_fitted = fitted.predict(validation_set[features])
	fit_score = accuracy_score(validation_set['diabetes'], pred_fitted)

	print("QuadraticDiscriminantAnalysis with features: age, pressure, triceps, mass" )
	print("Score: ""{0:.2f}".format(fit_score*100) + "%")


if __name__ == '__main__':


	Test()
