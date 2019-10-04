import pickle
import  numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# import some data to play with
iris = datasets.load_iris()
X = iris.data
y = iris.target
clf = LogisticRegression()
clf.fit(X,y)

flower = {0:'setosa',1:'versicolor',2:'virginica'}

# Saving model to disk
pickle.dump(clf, open('model.pkl','wb'))

test = np.array([6.3, 3.3, 6.1,2.5])
test = test.reshape(1, -1)

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
result = model.predict(test)
print(flower.get(result[0]))

