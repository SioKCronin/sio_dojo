# Central Limit Theorem Three
import math


n = 100
mean = 500
std = 80 / math.sqrt(n) #You divide by the square root of the population size, to take the population std and convert it into the sample std

x1 = (-1.96 * std) + mean 
x2 = (1.96 * std) + mean

print x1
print x2

