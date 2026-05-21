from math import *

f = lambda x: x**3 + x - 25
g = lambda x: 1/(x**2)
ForwardDiff = lambda pn, pn_1: pn_1 - pn


def AitkenMethod(init, iterationCount):
    numbers = []
    p0 = init
    p1 = f(p0)
    p2 = f(p1)
    for i in range(iterationCount):
        if abs(p2-2*p1+p0) >= 10**(-30):
            p0_hat = p0_hat = p0 - ((p1-p0)**2)/(p2-2*p1+p0)
            numbers.append(p0_hat)
            p0 = p0_hat
        else:
            numbers.append(p0)
        p1 = f(p0)
        p2 = f(p1)
    return numbers


def AitkenMethodSequence(iterationCount):
    numbers = []

    p0 = g(1)
    p1 = g(2)
    p2 = g(3)
    for i in range(iterationCount):
        if abs(p2-2*p1+p0) >= 10**(-30):
            p0_hat = p0_hat = p0 - ((p1-p0)**2)/(p2-2*p1+p0)
            numbers.append(p0_hat)
        else:
            numbers.append(p0)
        p0 = g(2+i)
        p1 = g(3+i)
        p2 = g(4+i)
    return numbers


def SteffensenMethod(init, iterationCount):
    numbers = []
    p0 = init
    p1 = f(p0)
    p2 = f(p1)
    for i in range(iterationCount):
        p0_hat = p0 - ((p1-p0)**2)/(p2-2*p1+p0)
        numbers.append(p0_hat)
        p0 = p0_hat
        p1 = f(p0)
        p2 = f(p1)
    return numbers


n = 10
# print("The first", f"{n}", "iterations of Aitken's method yields:", AitkenMethod(3, n+1))
print("The first", f"{n}", "iterations of Aitken's method for a sequence yields:", AitkenMethodSequence(n+1))
# print("The first", f"{n}", "iterations of Steffensen's method yields:", SteffensenMethod(3, n+1))
    

