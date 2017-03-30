# Binomial Distribution

import unittest
import math

n = 10
p = 0.12
q = 0.88

two = float("{0:.3f}".format(((math.factorial(10)/(math.factorial(2) * math.factorial(8))) * p**2 * q**8)))
one = float("{0:.3f}".format(((math.factorial(10)/(math.factorial(1) * math.factorial(9))) * p**1 * q**9)))
zero = float("{0:.3f}".format(((math.factorial(10)/(math.factorial(0) * math.factorial(10))) * p**0 * q**10)))


print two + one + zero
print 1 - (one + zero)

