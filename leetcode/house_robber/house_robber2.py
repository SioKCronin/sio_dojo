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

    x_steal, x_skip = 0, 0
    for x in l[:-1]:
        x_steal, x_skip = x + x_skip,  max(x_steal, x_skip)

    y_steal, y_skip = 0, 0
    for y in l[1:]:
        y_steal, y_skip = y + y_skip,  max(y_steal, y_skip)
    return max(max(x_steal, x_skip), max(y_steal, y_skip))

if __name__ == '__main__':
    unittest.main()
