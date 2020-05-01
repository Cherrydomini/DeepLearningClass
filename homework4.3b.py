import numpy as np
import math

x1 = float(input("please enter x1: "))
x2 = float(input("please enter x2: "))
yd1 = float(input("Desired Y1: "))
yd2 = float(input("Desired Y2: "))
a= .2
count = 1
w13 = .4
w23 = .2
w14 = -.5
w24 = .1
w35 = -.2
w45 = .4
w36 = .3
w46 = -.1


def bipolarsigmoid(x):
    return (2/(1 + math.exp(-a*x)))-1
def error(x,y):
    return y - x

def s(x,y):
    return x*(1-x)*y
def delta(x,y):
    return a*x*y
def theta(x):
    return a*-1*x
def change(x,y):
    return x+y

while count < 2:

        print("EPOCH: ", count)
        y3 =bipolarsigmoid(x1*w13+x2*w23)
        print("y3: ", y3)
        y4 = bipolarsigmoid(x1*w14+x2*w24)
        print("y4: ", y4)
        y5 = bipolarsigmoid(y3*w35+y4*w45)
        print("y5: ", y5)
        y6 = bipolarsigmoid(y3*w36 + y4*w46)
        print("y6: ", y6)
        e1 = error(y5, yd1)
        e2 = error(y6, yd2)
        print(yd1," - ", y5 ," = ", e1)
        print(yd2, " - ", y6, " = ", e2)


        s6 = s(y6, e2)
        print("s6: ", s6)
        s5 = s(y5, e1)
        print("s5: ", s5)
        s4 = s(y4, s6)
        print("s4: ", s4)
        s3 = s(y3, s5)
        print("s3: ", s3)


        dw36 = delta(y3,s6)
        dw46 = delta(y4, s6)
        dw35 = delta(y3, s5)
        dw45 = delta(y4, s5)
        dw13 = delta(x1, s3)
        dw23 = delta(x2, s3)
        dw14 = delta(x1, s4)
        dw24 = delta(x2, s4)

        print("deltaw13: ", dw13)
        print("deltaw23: ", dw23)
        print("deltaw14: ", dw14)
        print("deltaw24: ", dw24)
        print("deltaw35: ", dw35)
        print("deltaw45: ", dw45)
        print("deltaw36: ", dw36)
        print("deltaw46: ", dw46)


        w36 = change(w36, dw36)
        w46 = change(w46, dw46)
        w35 = change(w35, dw35)
        w45 = change(w45, dw45)
        w13 = change(w13, dw13)
        w23 = change(w23, dw23)
        w14 = change(w14, dw14)
        w24 = change(w24, dw24)


        print("w13: ", w13)
        print("w23: ", w23)
        print("w14: ", w14)
        print("w24: ", w24)
        print("w35: ", w35)
        print("w45: ", w45)
        print("w36: ", w36)
        print("w46: ", w46)
        count +=1
