import unittest
import itertools
import collections
import math

class TestPerfectSquares(unittest.TestCase):
    def test_simple_tree(self):
        self.assertEqual(perfect_squares(4), 1)
        self.assertEqual(perfect_squares(12), 3)

def perfect_squares(remainder, depth=0):
    if remainder == 0:
        return depth

    i = 1
    list_of_squares = []

    while i**2 <= remainder:
        list_of_squares.append(i**2)
        i+=1

    return min([perfect_squares(remainder-j, depth+1) for j in list_of_squares])

if __name__ == '__main__':
    unittest.main()
