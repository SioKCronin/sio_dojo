# Test Shut The Box

import unittest
from shut_the_box import Box, combinations

class TestBox(unittest.TestCase):
    def test_create_box(self):
        box = Box()

    def test_box_starting_value(self):
        box = Box()
        self.assertEqual(box.status, range(1,13))

class TestCombinations(unittest.TestCase):
    def test_combinations(self):
        self.assertEqual(combinations(7, [1,2,3, 4,5,6,7,8]),\
                set([(7,), (1, 6), (2, 5), (3, 4), (1, 2, 4)]))

if __name__ == '__main__':
    unittest.main()

