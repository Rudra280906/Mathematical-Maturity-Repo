import math
def LagrangeInterpolation(data, input):
    output = 0
    for i in data.keys():
        term = data[i]
        for j in data.keys():
            if j == i:
                continue
            term *= (input - j)/(i - j)
        output += term
    return output

def print2Darray(table):
    n = len(table)
    for i in range(n):
        for j in range(n):
            print(table[i][j], " ", end="")
        print("\n", end="")
    
def NevilleMethod(data, input):
    table = [[0 for i in range(len(data))] for j in range(len(data))]
    keys = list(data.keys())
    n = len(keys)
    for i in range(len(data)):
        table[i][0] = data[keys[i]]
    for i in range(1, n):
        for j in range(1, i+1):
            table[i][j] = ((input - keys[i-j])*table[i][j-1] - (input - keys[i])*table[i-1][j-1])/(keys[i]-keys[i-j])
    print2Darray(table)
    return table[n-1][n-1]
    
f = lambda x: math.sqrt(x)
inputs = [0, 1, 2, 4, 5]

# data = {8.1: 16.94410, 8.3: 17.56492, 8.6: 18.50515, 8.7: 18.82091}
data = {}
for i in inputs:
    data[i] = f(i)
input = 3
# print("Approximation via Lagrange Interpolation: ", LagrangeInterpolation(data, input))
print("Approximation via Neville's Method: ", NevilleMethod(data, input))