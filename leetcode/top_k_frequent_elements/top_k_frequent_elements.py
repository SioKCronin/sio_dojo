import unittest
from collections import Counter

class TestTopK(unittest.TestCase):

    def test_leet_examples(self):
        self.assertEqual(top_kth([1,1,1,2,2,3], k = 2), [1, 2])
        self.assertEqual(top_kth([1], k = 1), [1])

def top_kth(l, k):
    return [x for (x, y) in Counter(l).most_common(k)]

if __name__ == '__main__':
    unittest.main()

