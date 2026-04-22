from math import *
import sympy as sp
from sympy.abc import x

def NewtonMethod(err, initguess, function):
    p0 = initguess
    if (sp.diff(function).subs(x, p0) == 0):
        return "NULL"
    p1 = p0 - function.subs(x, p0)/sp.diff(function, x).subs(x, p0)
    count = 1
    while (abs(p1-p0) >= err):
        p0 = p1
        if (sp.diff(function).subs(x, p0) == 0):
            return "NULL"
        p1 = p0 - function.subs(x, p0)/sp.diff(function, x).subs(x, p0)
        if count >= 150:
            return "NULL"
        count += 1
    return p1, count


def ModifiedNewtonMethod(err, initguess, function):
    p0 = initguess
    if sp.diff(function, x).subs(x, p0) == 0:
        return "NULL"
    p1 = p0 - (function.subs(x, p0)*sp.diff(function, x).subs(x, p0))/((sp.diff(function, x).subs(x, p0))**2 - function.subs(x, p0)*sp.diff(function, x, 2).subs(x, p0))
    count = 1
    while (abs(p1-p0) >= err):
        p0 = p1
        if sp.diff(function, x).subs(x, p0) == 0:
            return "NULL"
        p1 = p0 - (function.subs(x, p0)*sp.diff(function, x).subs(x, p0))/((sp.diff(function, x).subs(x, p0))**2 - function.subs(x, p0)*sp.diff(function, x, 2).subs(x, p0))
        if count >= 150:
            return "NULL"
        count += 1
    return p1, count

print("The approximate value of the solution of x^2 - 2xe^(-x) + e^(-2x) = 0 \n"
      "and the number of iterations needed is:", NewtonMethod(10**(-5), 0.5, x**2 - 2*x*e**(-x) + e**(-2*x)))

print("The approximate value of the solution of x^2 - 2xe^(-x) + e^(-2x) = 0 \n"
      "and the number of iterations needed is:", ModifiedNewtonMethod(10**(-5), 0.5, x**2 - 2*x*e**(-x) + e**(-2*x)))
