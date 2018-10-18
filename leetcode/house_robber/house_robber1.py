'''
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint 
stopping you from robbing each of them is that adjacent houses have 
security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of
money of each house, determine the maximum amount of money you can 
rob tonight without alerting the police.

'''
import unittest

class TestHouseRobber1(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(rob([1, 4, 6, 7, 3]), 11)
        self.assertEqual(rob([1, 2, 3, 1]), 4)
        self.assertEqual(rob([2, 7, 9, 3, 1]), 12)

def rob(l):
    steal, skip = 0, 0
    for x in l:
        steal, skip = x + skip, max(steal, skip)
    return skip
    #return max(steal, skip)

if __name__ == '__main__':
    unittest.main()
