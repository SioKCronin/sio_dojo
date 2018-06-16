import math
import unittest


class TestBinarySearchIterative(unittest.TestCase):
    def test_contiguous_sorted(self):
        self.assertFalse(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
        self.assertTrue(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))

    def test_non_contiguous_sorted(self):
        self.assertFalse(binary_search([1, 2, 5, 8, 10, 13], 4))
        self.assertTrue(binary_search([1, 2, 5, 8, 10, 13], 8))

    def test_empty_list(self):
        self.assertFalse(binary_search([], 4))

    def test_all_same_number(self):
        self.assertTrue(binary_search([4, 4, 4, 4], 4))


def binary_search(sorted_list, target):

    length = len(sorted_list)

    while length > 0:

        if length == 1:
            if sorted_list[0] == target:
                return True
            else:
                return False

        if length >= 2:
            pivot = length // 2
            if target >= sorted_list[pivot]:
                sorted_list = sorted_list[pivot: None]
            else:
                sorted_list = sorted_list[None: pivot]
            length = len(sorted_list)

    return False


if __name__ == "__main__":
    unittest.main()
