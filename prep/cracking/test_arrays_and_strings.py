# Test Arrays and Strings

import unittest
from arrays_and_strings import *

class TestUnique(unittest.TestCase):
    def test_all_same(self):
        l = [1, 1, 1, 1, 1]
        self.assertEqual(unique(x), False)

if __name__ == '__main__':
    unittest.main()

