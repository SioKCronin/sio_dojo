# Question 2
'''
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
'''
import unittest

def question2(a):
    output = []
    i = 1
    for x in range((len(a)+1)):
        if a[x-i] == a[x]:
            if len(a[x-i:x]) > output:
                output = a[x-i:x]
        if a[x-i] == a[x+i]:
            while a[x-i] == a[x+i]:
                if len(a[x-i:x]) > output:
                    output = a[x-i:x]
                i += 1
        else:
            output = output
    return output

class TestQuestion2(unittest.TestCase):

    def test_no_palindrome_found(self):
        self.assertEqual(question2("1234568abc"), "")

    def test_palindrome_found(self):
        self.assertEqual(question2("abbaisgreat"), "abba")
        self.assertEqual(question2("abba2ablewasiereisawelba"), "ablewasiereisawelba")
        self.assertEqual(question2("24graba67b9"), "aba")
        self.assertEqual(question2("aa"), "aa")

if __name__ == '__main__':
    unittest.main()

