import numpy as np
import pandas as pd
from numpy.linalg import inv
import matplotlib.pyplot as plt
import random

data = pd.read_csv("learningcurves.txt")
data = data[['ln(y)','ln(X1)','ln(X2)']]
predict = 'ln(y)'
y = np.array(data[predict])
X1= np.array(data['ln(X1)'])
X2 = np.array(data['ln(X2)'])
ysum = np.sum(y)
x1sum = np.sum(X1)
x2sum = np.sum(X2)
size = len(y)

J = 0
B0 = 0
B1 = np.random.ranf()
B2 = np.random.ranf()

min = 0
max = 100
error = .25

done = 0.5
change = 200



while min < max:
    for i in range(size):
        n = 1
        n +i

        x1 = X1
        x2 = X2
        yi = y

        
        ybar = ysum/n
        x1bar = x1sum/n
        x2bar = x2sum / n

        cov1xy = (((x1[i] - x1bar) * (yi - ybar)) / n - 1)
        cov2xy = (((x2[i] - x2bar) * (yi - ybar)) / n - 1)
        varx1 = (((x1[i] - x1bar) ** 2) / (n))
        varx2 = (((x2[i] - x2bar) ** 2) / (n))
        B1 = ((cov1xy) / (varx1))
        B2 = ((cov2xy) / (varx2))
        B0 = ybar - (B1 * x1bar)


        newB1 = B1 - .1
        newB2 = B2 - .1
        J = ((.5) * (B0 + newB1 * X1[i] + newB2 * X2[i]) - y[i]) ** 2
        done = J
        print("FINAL J is: ", J)
        print(i)

    min+1
    print("FINAL J is ", J)


