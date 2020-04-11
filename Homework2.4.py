import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("tombstone", sep=";")
data = data[['S02', 'tomb']]

X = list(data['S02'])
Y = list(data['tomb'])
xsum = np.sum(X)
ysum = np.sum(Y)
size = len(data)

for i in range(size):
    n=1
    n +=i

    xi = X[i]
    yi = Y[i]
    xbar = xsum/n
    ybar = ysum/n

    covxy = (((xi-xbar)*(yi-ybar))/n-1)
    varx = (((xi - xbar)**2)/(n))
    coefficient = ((covxy)/(varx))
    intercept = ybar -(coefficient*xbar)



print("Coefficient: ", coefficient)
print("Intercept: ", intercept)


"""plt.scatter(X, Y)
plt.plot(X, reg.predict(X), color="blue")
plt.show()"""
##Should be: coefficient:  [0.00859333]
###intercept:  0.3229958988477033