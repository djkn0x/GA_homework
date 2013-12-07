from __future__ import division

import numpy as np
from sklearn import (metrics, cross_validation, linear_model, preprocessing)

SEED = 42

def load_data(filename, use_labels=True):
	data = np.loadtxt(open("data/" + filename), delimiter=',', usecols=range(1, 9), skiprows=1)
	if use_labels: 
		labels = np.loadtxt(open("data/" + filename), delimiter=',', usecols=[0], skiprows=1)
	else: 
		labels = np.zeros(data.shape[0])
	return labels, data

def save_results(predictions, filename):
	with open(filename, 'w') as f:
		f.write("id,Action\n")
		for i, pred in enumerate(predictions):
			f.write("%d,%f\n" % (i + 1, pred))

def main():
	for j in [1, 2, 3]:	
		model = linear_model.LogisticRegression(penalty='l1', C=j)

		# === load data in memory === #
		print "loading data for C=%d" % j
		y, X = load_data('train.csv')
		y_test, X_test = load_data('test.csv', use_labels=False)

		# === use on-hot encoding to encode category IDs === #
		encoder = preprocessing.OneHotEncoder()
		encoder.fit(np.vstack((X, X_test)))
		X = encoder.transform(X)
		X_test = encoder.transform(X_test)

		# === training and metrics === #
		mean_auc = 0.0

		n = 10
		for i in range(n):
			X_train, X_cv, y_train, y_cv = cross_validation.train_test_split(X, y, test_size=0.20, random_state=i*SEED)
			
			model.fit(X_train, y_train)
			preds = model.predict_proba(X_cv)[:, 1]

			fpr, tpr, thresholds = metrics.roc_curve(y_cv, preds)
			roc_auc = metrics.auc(fpr, tpr)
			mean_auc += roc_auc
		print "Mean AUC for C=%d: %f" % (j, mean_auc/n)

		# === Predictions === #
		model.fit(X, y)
		preds = model.predict_proba(X_test)[:, 1]
		filename = "submission%d" % j
		save_results(preds, filename + ".csv")

if __name__ == '__main__':
	main()
