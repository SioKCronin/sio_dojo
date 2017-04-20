# Weighted Mean

import unittest

def weighted_mean(n, x, w):
    product = [a*b for a,b in zip(x,w)]
    factorials = [x for x in w]
    print product
    print factorials
    return float(("{0:.1f}".format(float(sum(product))/float(sum(factorials)))))

class TestWeightedMean(unittest.TestCase):

    def test_simple_array(self):
        n = 5
        x = [10, 40, 30, 50, 20]
        w = [1, 2, 3, 4, 5]
        self.assertEqual(weighted_mean(n, x, w), 32.0)

    def test_longer_array(self):
        n = 10
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        w = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
        self.assertEqual(weighted_mean(n, x, w), 6.8)

    def test_fail_case(self):
        n = 20
        x = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        w = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 40, 30, 50, 20, 10, 40, 30, 50, 20]
        self.assertEqual(weighted_mean(n, x, w), 9.6)

if __name__ == '__main__':
    unittest.main()

'''

if __name__ == '__main__':
    n = int(raw_input())
    x = [int(i) for i in raw_input().split(" ")]
    w = [int(i) for i in raw_input().split(" ")]
    print weighted_mean(n, x, w)
'''
