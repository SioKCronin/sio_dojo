'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
'''

import unittest
import re

class TestValidPalindrome(unittest.TestCase):

    def test_leet_examples(self):
        self.assertTrue(valid_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(valid_palindrome("race a car"))
        self.assertFalse(valid_palindrome("ab"))
        self.assertFalse(valid_palindrome("abb"))
        self.assertFalse(valid_palindrome("0P"))


def valid_palindrome(phrase):
    letters = ''.join(e for e in phrase if e.isalnum()).lower()
    l = len(letters)
    if l <= 1:
        return True
    if l % 2 == 0:
        first = int((l / 2) - 1)
        second = int(l / 2)
    else:
        first = int(l // 2) 
        second = first
    for num in range(0, first+1): 
        if letters[first - num] != letters[second + num]:
            return False
    return True

if __name__ == '__main__':
    unittest.main()
