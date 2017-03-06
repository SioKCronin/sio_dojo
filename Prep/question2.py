# Question 2
'''
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
'''

def question2(a):
    def is_palindrome(x):
        output = []
        i = 1
        while l[x-i] == l[x+i]:
            output = l[x-i:x+i]

    def test_longest_palindrome(a):
        output = []

        for x in a:
            output.append(is_palindrome(x)):
        return str(max(output))


class TestQuestion2(unittest.TestCase):

    def test_no_palindrome_found(self):
        self.assertEqual(question2("1234568abc"), "")

    def test_palindrome_found(self):
        self.assertEqual(question2("abbaisgreat"), "abba")
        self.assertEqual(question2("abba2ablewasiereisawelba"), "ablewasiereisawelba")
        self.assertEqual(question2("24graba67b9"), "aba")
        self.assertEqual(question2("aa"), "aa")


