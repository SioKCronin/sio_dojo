"""
A function g(n) is defined by:
g(n) = n if n < 3, and g(n) = g(n-1) + 2*g(n-2) + 3*g(n-3) if n >= 3

Write a recursive implementation of g(n) called g_recursive(n).
Write an iterative implementation of g(n) called g_iterative(n).
"""
def g_recursive(n):
    n = float(n)
    if n < 3:
        return n
    else:
        return g_recursive(n-1) + 2*g_recursive(n-2) + 3*g_recursive(n-3)

def g_iterative(n):
    n = float(n)
    if n >= 3:
        count = 0
        while n >= 3:
            if (n-1) < 3 and (n-2) < 3 and (n-3) < 3:
                count = count + (n-1) + 2*(n-2) + 3*(n-3)
                return count
            else:
                if (n-2) < 3 and (n-3) < 3:
                    count = count + (n-1) + 2*(n-2) + (n-2)
                    return count
                else:
                    if (n-3) < 3:
                        count = count + (n-1) + 2*(n-2) + 3*(n-3) + (n-2) + \
                                2*(n-3) + (n-3)
                        return count
                    else:
                        count = count + (n-1) + 2*(n-2) + 3*(n-3)
                        n = n-1
    else:
        return n

# TEST

import unittest

class TestFunctions(unittest.TestCase):

    def test_recursive(self):
        self.assertEqual(g_recursive(0), 0)
        self.assertEqual(g_recursive(5), 25)
        self.assertEqual(g_recursive(10), 1892)
        self.assertEqual(g_recursive(3.14), 4.84)

    def test_iterative(self):
        self.assertEqual(g_iterative(0), 0)
        self.assertEqual(g_iterative(5), 25)
        self.assertEqual(g_recursive(10), 1892)
        self.assertEqual(g_iterative(3.14), 4.84)

if __name__ == '__main__':
    unittest.main()
