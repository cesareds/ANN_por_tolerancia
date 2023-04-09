import math
from scipy import *
from sympy import *
from numpy import *

PI = 3.14159265359
SIZE1 = 4
SIZE2 = 3
SIZE3 = 3
SIZE4 = 4


def bis(f, a, b, n, p):
    iteracao = 0
    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        print("Voce nao pode usar esse intervalo\n")
        return
    else:
        m = 0.5 * (a + b)
        while tol < abs(f(m)):
            m = 0.5 * (a + b)
            fm = f(m)
            if fm == 0:
                print("Voce encoutrou uma raiz r=%.16f\n" % m)
                return

            # print("%.16f,\n" % m)
            # print(iteracao)

            iteracao += 1
            if fa * fm < 0:
                b = m
            else:
                a = m
                fa = fm
        print(iteracao)
        print(",%.16f,\n" % m)



def newton(f, df, x0, n):
    iteracao = 0
    while tol < abs(f(x0)):
        dfx0 = df(x0)
        if dfx0 == 0:
            break
        xi = x0 - f(x0) / dfx0

        # print("%.16f,\n" % xi)
        # print(iteracao)

        iteracao += 1
        x0 = xi
    print(iteracao)
    print(",%.16f,\n" % xi)



def secant(f, x0, x1, n):
    iteracao = 0
    while tol < abs(f(x0)):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx0 == fx1:
            break
        x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)
        # print("%.16f,\n" % x2)
        # print(iteracao)
        iteracao += 1
        x0 = x1
        x1 = x2
    print(iteracao-1)
    print(",%.16f,\n" % x2)



def false_position(f, a, b, tol, n):
    fa = f(a)
    fb = f(b)
    iteracao = 0
    if fa * fb >= 0:
        print(f"O Teorema de Bolzano não sabe dizer se existe raiz para f no intervalo [{a:.16f}, {b:.16f}]")
        return
    else:
        x = (a * fb - b * fa) / (fb - fa)
        while tol < abs(f(x)):
            x = (a * fb - b * fa) / (fb - fa)
            # print("%.16f,\n" % x)
            # i2 += 1
            iteracao += 1
            fx = f(x)
            if fx == 0:
                print("Encontramos uma raiz para f, ela é x = %.16f" % x)
                return
            if fa * fx < 0:
                b = x
                fb = fx
            else:
                a = x
                fa = fx
    print(iteracao)
    print(",%.16f,\n" % x)



def f(x):
    return x**x-2


def d_f(x):
    return (x**x)*(ln(x) + 1)

tol = 1.43118e-08
data = {'false_position': {'a': 0.598018, 'b': 2.154695}, 'newton': {'x0': 3.322062}, 'bisection': {'a': 0.988093, 'b': 5.600357}, 'secant': {'x0': 0.707542, 'x1': 2.97655}}


n = 100
# print("\nbis:\n")
bis(f, data['bisection']['a'], data['bisection']['b'], n, tol)
# print("\nnewton:\n")
newton(f, d_f, data['newton']['x0'], n)
# print("\nsecant:\n")
secant(f, data['secant']['x0'], data['secant']['x1'], n)
# print("\nfalse_position:\n")
false_position(f, data['false_position']['a'], data['false_position']['b'], tol, n)
