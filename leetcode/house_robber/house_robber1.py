import unittest

class TestHouseRobber1(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(rob([1, 4, 6, 7, 3]), 11)
        self.assertEqual(rob([1, 2, 3, 1]), 4)
        self.assertEqual(rob([2, 7, 9, 3, 1]), 12)

def rob(l):
    steal, skip = 0, 0
    for x in l:
        steal, skip = x + skip,  max(steal, skip)
    return max(steal, skip)

if __name__ == '__main__':
    unittest.main()



