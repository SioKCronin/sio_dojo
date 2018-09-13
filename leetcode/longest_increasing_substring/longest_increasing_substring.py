import unittest

class TestLongestIncreasingSubstring(unittest.TestCase):

    def test_leet_examples(self):
        self.assertEqual(longest_increasing_substring([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(longest_increasing_substring([10, 9, 2, 5, 3]), 2)
        self.assertEqual(longest_increasing_substring([2, 5, 3, 4]), 3)
        self.assertEqual(longest_increasing_substring([10, 9, 2, 5, 3, 4]), 3)
        self.assertEqual(longest_increasing_substring([1, 3, 6, 7, 9, 4, 10, 5, 6]), 6)

def longest_increasing_substring(s):
    if not s: return 0
    memo = [0] * len(s)
    memo[0] = 1
    for i in range(len(s)):
        max_value = 0
        for j in range(len(s[:i])):
            if s[i] > s[j]:
                max_value = max(max_value, memo[j])
        memo[i] = max_value + 1
    return max(memo)

if __name__ == '__main__':
    unittest.main()
