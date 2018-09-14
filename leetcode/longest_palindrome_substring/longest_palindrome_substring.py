import unittest

class TestLogestPalindromeSubstring(unittest.TestCase):

    def test_leet_examples(self):
        self.assertEqual(longest_palindrome("babad"), "bab")
        self.assertEqual(longest_palindrome("cbbd"), "bb")

def longest_palindrome(s):
    if len(s) == 0: return 0
    if len(s) == 1: return 1
    longest = ""
    memo = [0]*len(s)
    memo[0] = 1
    for i in range(len(s)):
        sub_longest = ""
        path = s[:i]
        while path:
            for j in range(1, len(s[:i])):
                letter = path.pop()
                if s[i+j] == letter: 
                    print("Found it!")
                    sub_longest = s[i-j:i+j+1]
            if len(sub_longest) > len(longest):
                longest = sub_longest

if __name__ == '__main__':
    unittest.main()
