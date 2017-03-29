# Poisson Distribution
import math

x = 0.88
y = 1.55

A = 160 + 40 * (x + x**2)
B = 128 + 40 * (y + y**2)

print round(A, 3)
print round(B, 3)

'''
def poisson_distribution(l, k):
    return (l**k * 1/e**l) / math.factorial(k)

result = poisson_distribution(l, k) 

print round(result, 3)
'''
