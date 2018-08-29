import unittest
from collections import Counter

class TestFindDifference(unittest.TestCase):

    def test_leet_example(self):
        self.assertEqual('e', find_difference('abcd', 'abcde'))

    def test_my_examples(self):
        self.assertEqual('a', find_difference('abcd', 'aabcd'))
        self.assertEqual('f', find_difference('abcd', 'abcfd'))

def find_difference(s, t):
    first = Counter(list(s))
    second = Counter(list(t))
    diff = second-first
    return list(diff.elements())[0]

if __name__ == '__main__':
    unittest.main()
