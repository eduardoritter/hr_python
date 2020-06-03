'''
Binomial Distribution

The number of successes is x.
The total number of trials is n.
The probability of success of 1 trial is p.
The probability of failure of 1 trial q, where q = 1 - p.
 '''
from math import factorial

def combination(n, x):
    return factorial(n) / (factorial(x) * factorial(n-x))


def binomial(x, n, p):
    return combination(n, x) * (p ** x) * ((1-p) ** (n-x))


#p, batch_size = list(map(int, input().split(" ")))
#ratio = p/100

ratio = 0.12
batch_size = 10

probability = 0

#Probability no more than 2 rejects
for x in range(3):
    probability += binomial(x, batch_size, ratio)

print("%.3f" % probability)

probability = 0

#Probability at least 2 rejects
for x in range(2, batch_size + 1):
    probability += binomial(x, batch_size, ratio)

print("%.3f" % probability)