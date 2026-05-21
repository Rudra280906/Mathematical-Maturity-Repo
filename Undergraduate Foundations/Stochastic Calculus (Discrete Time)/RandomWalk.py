import random

def RandomWalk(M_i):
    X_n = random.random()
    M_i2 = M_i
    if X_n >= 0.5:
        M_i2 += 1 # Heads
    else:
        M_i2 -= 1 # Tails
    return M_i2

sum = 0
n = 1000
trials = 20000
random_variables = [] #Simulates X_1, X_2, ..., X_n
for i in range(n): 
    x = random.random()
    if x >= 0.5:
        random_variables.append(1) # Heads
    else:
        random_variables.append(-1) # Tails
# E[X_i] = 0.5*1 + 0.5*(-1) = 0
M_i = 0
for i in random_variables:
    M_i += i

for i in range(trials):
    trial = RandomWalk(M_i)
    sum += trial
print(f"M_{n} = ", M_i)
print("For", f"M_{n+1}", "using", f"{trials} trials","simulating a random walk, the average was", sum/trials)