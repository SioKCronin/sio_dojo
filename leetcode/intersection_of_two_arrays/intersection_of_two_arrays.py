import unittest

'''
Return the unique integers in the intersection of two lists.
'''

class TestIntersection(unittest.TestCase):

    def test_leet(self):
        self.assertEqual(intersect_lists([1, 2, 2, 1], [2, 2]), [2])
        self.assertEqual(intersect_lists([4, 9, 5], [9, 4, 9, 8, 4]), [9, 4])

def intersect_lists(l1, l2):
    first = set(l1)
    second = set(l2)
    return list(first.intersection(second))

if __name__ == "__main__":
    unittest.main()
