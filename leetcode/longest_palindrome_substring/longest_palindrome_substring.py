import unittest

class TestLogestPalindromeSubstring(unittest.TestCase):

    def test_leet_examples(self):
        self.assertEqual(longest_palindrome("babad"), "bab")
        self.assertEqual(longest_palindrome("cbbd"), "bb")

def longest_palindrome(s):
    if len(s) == 0: return 0
    if len(s) == 1: return 1
    longest = ""
    path = [s[0]]
    for i in range(1, len(s)):
        for j in range(i+1, len(s)):
            first = s[i:][j-i]
            second = path[-(j-i)]
            print("first", first)
            print("second", second)
            if j >= len(path):
                break
            if first == second:
                print("Found it")
        path = [i] + path
    return longest

if __name__ == '__main__':
    unittest.main()
