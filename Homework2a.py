import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

y = np.array([[78.93], [58.20], [67.47], [37.47], [45.65], [32.92], [29.97]])
x = np.array([[1.17], [2.97], [3.26], [4.69], [5.83], [6.00], [6.41]])

reg = linear_model.LinearRegression().fit(x, y)
print(reg.coef_)
print(reg.intercept_)

plt.scatter(x, y)
plt.plot(x, reg.predict(x), color="blue")
plt.show()

