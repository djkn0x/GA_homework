import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import StratifiedKFold

# Import Iris dataset and assign variables
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Use standard KNN classifier with different n_neighbors
for n in range(1,20):
                                                          
    knn = KNeighborsClassifier(n_neighbors=n, algorithm='auto')
    print "KNN with %d neighbors" % n

    # Use StratifiedKFold approach, with different n_folds, to select training and test datasets
    for i in [2, 3, 4, 5, 10]:
        kf = StratifiedKFold(y, n_folds=i)
        score = []
        for train, test in kf: 
            knn.fit(X[train], y[train])
            score.append(knn.score(X[test], y[test]))

        # Set score as average scores across each i n_folds
        score = np.mean(score)
        print("%d folds: %f%% accuracy" % (i, score))

    print "\r"
