import unittest

class TestFindSum(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_sum([1,3,4,5], 6), [1,5])

def find_sum(l: list, k: int) -> list:


if __name__ == '__main__':
    unittest.main()