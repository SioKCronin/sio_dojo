import math
import unittest


class TestBinarySearch(unittest.TestCase):
    def test_contiguous_sorted(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, None, None))
        self.assertTrue(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, None, None))

    def test_non_contiguous_sorted(self):
        sorted_list2 = [1, 2, 5, 8, 10, 13]
        binary_search(sorted_list2, 4, None, None)
        self.assertFalse(binary_search([1, 2, 5, 8, 10, 13], 4, None, None))
        self.assertTrue(binary_search([1, 2, 5, 8, 10, 13], 8, None, None))

    def test_empty_list(self):
        self.assertFalse(binary_search([], 4, None, None))

    def test_all_same_number(self):
        self.assertTrue(binary_search([4, 4, 4, 4], 4, None, None))


def binary_search(sorted_list, target, start, end):

    sorted_list = sorted_list[start:end]
    length = len(sorted_list)

    if length == 0:
        return False

    if length == 1:
        if sorted_list[0] == target:
            return True
        else:
            return False

    if length % 2 == 1:
        pivot = length // 2
        if target >= sorted_list[pivot]:
            return binary_search(sorted_list, target, pivot, None)
        if target < sorted_list[pivot]:
            return binary_search(sorted_list, target, None, pivot)
    else:
        pivot = int(length / 2)
        if target >= sorted_list[pivot]:
            return binary_search(sorted_list, target, pivot, None)
        if target < sorted_list[pivot]:
            return binary_search(sorted_list, target, None, pivot)


if __name__ == "__main__":
    unittest.main()
