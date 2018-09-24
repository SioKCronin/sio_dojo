import unittest
from collections import Counter

class TestSingleNumber(unittest.TestCase):

    def test_leet_examples(self):
        self.assertEqual(single_number([2, 2, 1]), 1)
        self.assertEqual(single_number([4, 1, 2, 1, 2]), 4)

def single_number(l):
    c = Counter(l)
    return c.most_common()[-1][0]

if __name__ == '__main__':
    unittest.main()
