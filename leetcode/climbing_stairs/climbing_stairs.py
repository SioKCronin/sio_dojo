import unittest

class TestClimbingStairs(unittest.TestCase):

    def test_leet_examples(self):
        self.assertEqual(stair_paths(2), 2)
        self.assertEqual(stair_paths(3), 3)
        self.assertEqual(stair_paths(4), 5)

    def test_dp(self):
        self.assertEqual(dp_stair_paths(2), 2)
        self.assertEqual(dp_stair_paths(3), 3)
        self.assertEqual(dp_stair_paths(4), 5)

def stair_paths(n):
    if n <= 1: return 1
    return stair_paths(n-1) + stair_paths(n-2)

def dp_stair_paths(n, memo=[0]*1000000):
    if n <= 1:return 1
    if memo[n] == 0:
        memo[n] = dp_stair_paths(n-1) + dp_stair_paths(n-2)
    return memo[n]

if __name__ == '__main__':
    unittest.main()

