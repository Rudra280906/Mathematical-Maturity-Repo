import math
import sympy as sp
from sympy.abc import x


def Function(x):
    return x - 2**(-x)


def BisectionMethod(error, a, b, function):
    n = math.ceil(math.log2((b-a)/error))
    p = (a + b) / 2
    for i in range(n):
        p = (a + b) / 2
        sign = 0
        f_value_a = function.subs(x, a)
        f_value_b = function.subs(x, b)
        f_value_p = function.subs(x, p)
        if f_value_a > 0:
            sign = 1
        if sign == 0:
            if f_value_p < 0:
                a = p
            if f_value_p > 0:
                b = p
        if sign == 1:
            if f_value_p < 0:
                b = p
            if f_value_p > 0:
                a = p
    return p


print(BisectionMethod(10**-5, 0, 1, x - 2**(-x)))
