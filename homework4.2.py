import numpy as np
import math

x1 = float(input("please enter x1"))
x2 = float(input("please enter x2"))
yd = float(input("What is the desired output: "))
a= .1
count = 1
w13 = .6
w23 = .3
w14 = .8
w24 = 1.1
w35 = 1.2
w45 = 1.0
theta3 = .7
theta4 = .2
theta5 = .4

def sigmoid(x):
    return 1/(1+ math.exp(-x))
def error(x):
    return yd - x
def s(x,y):
    return x*(1-x)*y
def delta(x,y):
    return a*x*y
def theta(x):
    return a*-1*x
def change(x,y):
    return x+y


while count < 5:
        print("EPOCH: ", count)
        y3 =sigmoid(x1*w13+x2*w23-theta3)
        print("y3: ", y3)
        y4 = sigmoid(x1*w14+x2*w24-theta4)
        print("y4: ", y4)
        y5 = sigmoid(y3*w35+y4*w45-theta5)
        print("y5: ", y5)
        e = yd - y5
        print("e: ", e)





        s5 = s(y5, e)
        print("s5: ", s5)
        s3 = s(y3, s5)
        print("s3: ", s3)
        s4 = s(y4, s5)
        print("s4: ", s4)

        dw35 = delta(y3, s5)
        dw45 = delta(y4, s5)
        dw13 = delta(x1, s3)
        dw23 = delta(x2, s3)
        dw14 = delta(x1, s4)
        dw24 = delta(x2, s4)
        dtheta5 = theta(s5)
        dtheta3 = theta(s3)
        dtheta4 = theta(s4)

        w35 = change(w35, dw35)
        w45 = change(w45, dw45)
        theta5 = change(theta5, dtheta5)
        w13 = change(w13, dw13)
        w23 = change(w23, dw23)
        theta3 = change(theta3, dtheta3)
        w14 = change(w14, dw14)
        w24 = change(w24, dw24)
        theta4 = change(theta4, dtheta4)

        print("w13: ", w13)
        print("w23: ", w23)
        print("w14: ", w14)
        print("w24: ", w24)
        print("w35: ", w35)
        print("w45: ", w45)
        print("theta3: ", theta3)
        print("theta4: ", theta4)
        print("theta5: ", theta5)
        count +=1
