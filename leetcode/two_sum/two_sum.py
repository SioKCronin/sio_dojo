import unittest
from collections import defaultdict
import math

class TestTwoSum(unittest.TestCase):

    def test_leet_example(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([-1,-2,-3,-4,-5], -8), [2, 4])

    def test_leet_example(self):
        self.assertEqual(two_sum_hash([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum_hash([-1,-2,-3,-4,-5], -8), [2, 4])

# Brute force
def two_sum(nums, target):
    sample = 0
    if target >= 0:
        sample = target + 1
    else:
        sample = target - 1
    for i, first in enumerate(nums):
        for j, second in enumerate(nums[:i] + [sample] + nums[i+1:]):
            if first + second == target:
                return [i, j]

# Refactored for time
def two_sum_hash(nums, target):
    lookup = {}
    for i, first in enumerate(nums):
        if target - first in lookup:
            return [lookup[target-first], i]
        else:
            lookup[first] = i

if __name__ == '__main__':
    unittest.main()
