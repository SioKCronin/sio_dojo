'''
Given a non-empty string s, you may delete at most one character. 
Judge whether you can make it a palindrome.

The key insight below is that if we get thorugh the for loop, then all the 
terminal points matched. Otherwise, we're testing if we can remove a char
at the beginning or end to make a palindrome. 
'''
import unittest

class TestValidPalindrome(unittest.TestCase):

    def test_leet_examples(self):
        self.assertTrue(delete_one_vp("aba"))
        self.assertTrue(delete_one_vp("abca"))
        self.assertTrue(delete_one_vp("eccer"))
        self.assertFalse(delete_one_vp("edcer"))


def delete_one_vp(s):
    def is_pali_range(i, j):
        return all(s[k] == s[j-k+i] for k in range(i, j))

    flag = True

    for i in range(int(len(s) / 2)):
        if s[i] != s[~i]:
            j = len(s) - 1 - i
            flag = is_pali_range(i+1, j) or is_pali_range(i, j-1)
    return flag

if __name__ == '__main__':
    unittest.main()
