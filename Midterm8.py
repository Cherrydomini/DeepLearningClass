#PART A
from __future__ import absolute_import, division, print_function, unicode_literals
from os.path import dirname, join as pjoin
import scipy.io as sio
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras import regularizers

data = sio.loadmat("notMNIST_small.mat")
#find the name of the columns to make an array for the images and labels
print(data.keys())
print("number of images: ", len(data))

x = data['images']
x = x.transpose()
print(x.shape)
y = data['labels']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#PART B
#mean subtraction
x_train = x_train - x_train.mean()
x_test = x_test - x_test.mean()
#normalization
x_train = x_train/x_train.std()
x_test = x_test/x_test.std()

print("Training data stats:\n", "min: ",x_train.min(), "max: ", x_train.max(), "mean: ", x_train.mean(), "std: ", x_train.std())
print("Testing data stats:\n", "min: ",x_test.min(), "max: ", x_test.max(), "mean: ", x_test.mean(), "std: ", x_test.std())


model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
#PART C, D, & Initialization, number of layers, and activation function
model.add(tf.keras.layers.Dense(128, activation='relu', kernel_initializer="glorot_normal"))
#PART G regularization techniques
model.add(tf.keras.layers.Dense(10, activation="softmax", activity_regularizer=regularizers.l1_l2(l1=1e-5, l2=1e-4)))

#PART E GRADIENT OPTIMIZATION TECHNIQUE
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metric=['accuracy'])

model.fit(x_train, y_train, epochs = 10)

model.evaluate(x_test,  y_test, verbose=2)
model.summary()