# Question 1
'''
Given two strings s and t, determine whether some anagram of t is a substring of s.
For example: if s = "udacity" and t = "ad", then the function returns True.
Your function definition should look like: question1(s, t) and return a boolean True or False.
'''
import unittest

def question1(s, t):
    import itertools
    options = list(itertools.permutations(t))
    for x in options:
        if ''.join(x) in s:
            return True
    return False

class TestQuestion1(unittest.TestCase):
    def test_valid_substring(self):
        self.assertEqual(question1("udacity", "ad"), True)
        self.assertEqual(question1("super88", "pre8u"), True)
        self.assertEqual(question1("udacity", ""), True)

    def test_not_valid_substring(self):
        self.assertEqual(question1("udacity", "yu"), False)
        self.assertEqual(question1("super88", "8epsu"), False)

if __name__ == '__main__':
    unittest.main()

