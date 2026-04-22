import math
import sympy as sp
from sympy.abc import x


def FixedPointIteration(err, function):
    count = 0
    p = 1
    p_ = function.subs(x, p)
    while abs(p_ - p) >= err:
        p = p_
        p_ = function.subs(x, p)
        count += 1
        if count >= 2**20:
            break
    return count

print("The number of iterations to get within 10^(-5) is", FixedPointIteration(10**(-5), ((3+x-2*x**2)**(1/4)) ))

