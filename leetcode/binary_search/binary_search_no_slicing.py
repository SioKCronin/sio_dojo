import math
import unittest


class TestBinarySearch(unittest.TestCase):
    def test_contiguous_sorted(self):
        self.assertTrue(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
        self.assertTrue(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))

    def test_non_contiguous_sorted(self):
        self.assertFalse(binary_search([1, 2, 5, 8, 10, 13], 4))
        self.assertTrue(binary_search([1, 2, 5, 8, 10, 13], 8))

    def test_empty_list(self):
        self.assertFalse(binary_search([], 4)) 

    def test_all_same_number(self):
        self.assertTrue(binary_search([4, 4, 4, 4], 4))


def binary_search(sorted_list, target, low=0, high=None):
    if high == None:
        high = len(sorted_list) - 1

    if not sorted_list:
        return False

    if high - low <= 1:
        if sorted_list[low] == target or sorted_list[high] == target:
            return True
        return False

    pivot = ((high - low) // 2) + low

    if target >= sorted_list[pivot]:
        return binary_search(sorted_list, target, pivot, high)
    if target < sorted_list[pivot]:
        return binary_search(sorted_list, target, low, pivot)


if __name__ == "__main__":
    unittest.main()
