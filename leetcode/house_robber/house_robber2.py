import unittest

class TestHouseRobber2(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(rob_two([]), 0)
        self.assertEqual(rob_two([1]), 1)
        self.assertEqual(rob_two([1, 2]), 2)
        self.assertEqual(rob_two([1, 1, 1]), 1)
        self.assertEqual(rob_two([2, 3, 2]), 3)
        self.assertEqual(rob_two([1, 2, 3, 1]), 4)
        self.assertEqual(rob_two([1, 2, 1, 1]), 3)

def rob_two(l):
    if not l:
        return 0
    if len(l) <= 2:
        return max(l)
    steal, skip = 0, 0
    for x in l:
        steal, skip = x + skip,  max(steal, skip)
        print("Steal: ", steal)
        print("Skip: ", skip)
    x_steal, x_skip = l[0] + skip, max(steal, skip)
    if x_steal > x_steal:
        return skip
    return steal

if __name__ == '__main__':
    unittest.main()
