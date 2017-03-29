# Poisson Distribution
import math

l = 2.5
k = 5
e = math.exp(1)

def poisson_distribution(l, k):
    return (l**k * 1/e**l) / math.factorial(k)

result = poisson_distribution(l, k) 

print round(result, 3)
