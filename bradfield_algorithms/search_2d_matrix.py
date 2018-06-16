import unittest
import math

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]


class Solution(object):
    def searchMatrix(self, matrix, target, start, end):
        matrix = matrix[start:end]
        length = len(matrix)

        if length == 0:
            return False
        if length == 1:
            if target in matrix[0]:
                return True
            return False

        midpoint = length // 2

        if target < matrix[midpoint][0]:
            return self.searchMatrix(matrix, target, None, midpoint)
        else:
            return self.searchMatrix(matrix, target, midpoint, None)


class TestSearch(unittest.TestCase):
    def test_search(self):
        s = Solution()
        self.assertTrue(s.searchMatrix(matrix, 3, None, None))
        self.assertFalse(s.searchMatrix(matrix, 13, None, None))


if __name__ == "__main__":
    unittest.main()
