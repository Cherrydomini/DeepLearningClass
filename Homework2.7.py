from numpy import array
from numpy.linalg import inv
from matplotlib import pyplot
import numpy as np
import pandas as pd
data = pd.read_csv("learningcurves.txt")
data = data[['ln(y)','ln(X1)','ln(X2)']]
predict = 'ln(y)'
y = np.array(data[predict])
X= np.array(data[(['ln(X1)','ln(X2)'])])
x1 = np.array(data[['ln(X1)']])
x2 = np.array(data[['ln(X2)']])
X = X.reshape((len(X), -1))

# linear least squares
b = inv(X.T.dot(X)).dot(X.T).dot(y)
print(b)
# predict using coefficients
yhat = X.dot(b)
# plot data and predictions
pyplot.scatter(x1, y)
pyplot.plot(X, yhat)
pyplot.show()