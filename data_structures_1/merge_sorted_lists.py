import unittest

class TestMergeSorted(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(merge_sorted([], []), [])
        self.assertEqual(merge_sorted([1,3,5], [2,4]), [1, 2, 3, 4, 5])

def merge_sorted(lst1: list, lst2: list) -> list:
    result = lst1 + lst2
    result.sort()
    return result

if __name__ == '__main__':
    unittest.main()