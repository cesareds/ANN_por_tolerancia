import math
from scipy import *
from sympy import *

PI = 3.14159265359
SIZE1 = 4
SIZE2 = 3
SIZE3 = 3
SIZE4 = 4


def bis(f, a, b, n, p):
    iteracao = 1
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
        print("%.16f,\n" % m)
        print(iteracao)


def newton(f, df, x0, n):
    iteracao = 1
    while tol < abs(f(x0)):
        dfx0 = df(x0)
        if dfx0 == 0:
            break
        xi = x0 - f(x0) / dfx0

        # print("%.16f,\n" % xi)
        # print(iteracao)

        iteracao += 1
        x0 = xi
    print("%.16f,\n" % xi)
    print(iteracao)


def secant(f, x0, x1, n):
    iteracao = 1
    i2 = 0
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
    print("%.16f,\n" % x2)
    print(iteracao)


def false_position(f, a, b, tol, n):
    fa = f(a)
    fb = f(b)
    iteracao = 1
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
    print("%.16f,\n" % x)
    print(iteracao)


def f(x):
    return math.exp(3*x)-5


def d_f(x):
    return 3*math.exp(3*x)

tol = 1.55836e-09

a_bisection = -0.44225
b_bisection = 2.037105

x0_newton = 1.660578

x0_secant = -0.49591
x1_secant = 1.254506

b_false_position = -0.929181
a_false_position = 1.053206


n = 100
print("\nbis:\n")
bis(f, a_bisection, b_bisection, n, tol)
print("\nnewton:\n")
newton(f, d_f, x0_newton, n)
print("\nsecant:\n")
secant(f, x0_secant, x1_secant, n)
print("\nfalse_position:\n")
false_position(f, a_false_position, b_false_position, tol, n)