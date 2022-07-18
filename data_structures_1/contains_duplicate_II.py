import unittest

class TestDuplicates(unittest.TestCase):

    def test_single(self):
        self.assertTrue(containsNearbyDuplicates([1, 1], 2))
        self.assertTrue(containsNearbyDuplicates([1,0,1,1], 1))
        self.assertTrue(containsNearbyDuplicates([99, 99], 2))
        self.assertFalse(containsNearbyDuplicates([1,2,3,1,2,3], 2))

def containsNearbyDuplicates(nums: list, k: int) -> bool:

    # To limit searching, I'd like to compare against j's up to k
    # and then evaluate a k-sized window between i-j 

    for i in range(len(nums)):
        for j in range(k+1):
            print((i, j))
            if (i != j) and (nums[i] == nums[i-j]):
                return True
    return False

if __name__ == '__main__':
    unittest.main()