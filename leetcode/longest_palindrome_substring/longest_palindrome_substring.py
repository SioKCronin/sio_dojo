import unittest

class TestLogestPalindromeSubstring(unittest.TestCase):

    def test_leet_examples(self):
        self.assertEqual(longest_palindrome("babad"), "bab")
        self.assertEqual(longest_palindrome("cbbd"), "bb")

def longest_palindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r -= 1
    return s[l:r+1]

def longest_palindrome(s):
    longest = ''

    for i in range(len(s)):
        # handle the odd case 
        odd = longest_palindrome(s, i, i)

        # handle the even case
        even = longest_palindrome(s, i, i+1)


if __name__ == '__main__':
    unittest.main()
