# Binomial Distribution

import unittest
import math

def binomial_distribution():
    n = 6
    x = 3
    p = 1.09/2.09
    q = 1 - p

    three = float("{0:.3f}".format(((math.factorial(n)/(math.factorial(3) * math.factorial(3))) * p**3 * q**3)))
    four = float("{0:.3f}".format(((math.factorial(n)/(math.factorial(4) * math.factorial(2))) * p**4 * q**2)))
    five = float("{0:.3f}".format(((math.factorial(n)/(math.factorial(5) * math.factorial(1))) * p**5 * q**1)))
    six = float("{0:.3f}".format(((math.factorial(n)/(math.factorial(6) * math.factorial(0))) * p**6 * q**0)))

    return three + four + five + six

class TestBinomialDistribution(unittest.TestCase):

    def test_short_array(self):
        self.assertEqual(binomial_distribution(), 13)
'''
if __name__ == '__main__':
    unittest.main()
'''
if __name__ == '__main__':
    print binomial_distribution()
