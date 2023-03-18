from sympy import *
import numpy as np


def newton(f, df, x0, n, iterations):
    iter = 1
    i2 = 0
    for i in range(n+1):

        dfx0 = df(x0)
        if dfx0 == 0:
            print("derivative == 0")
            break

        xi = x0 - f(x0) / dfx0

        if iterations.__contains__(i):
            print("AAAAA:\t" +  str(xi))
            print(xi)
        x0 = xi

        print("i: "+ str(i) + "\tx0: " + str(x0) + "\tdfx0: " + str(dfx0) + "\tfx0: " + str(f(x0)) + "")

iterations = {1, 3, 5}


def f(x):
    return x - pow(2, -x)


def df(x):
    return 1 + ln(2) * 2**-x


x0 = 0.23216
n = 5
newton(f, df, x0, n, iterations)
