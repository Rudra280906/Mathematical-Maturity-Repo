# coeff is [an, a_{n-1}, ..., a0]
# returns [bn, ..., b0]


def HornerMethod(coeff, x0):
    coeff2 = [coeff[0]]
    n = len(coeff)
    for i in range(1, n):
        b = coeff[i] + coeff2[-1]*x0
        coeff2.append(b)
    return coeff2


c = [2, 0, -3, 3, -4]
print("Original polynomial: ", c)
print("New polynomial: ", HornerMethod(c, -2))


