# Question 2
'''
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
'''

def question2(a):
    pass

class TestQuestion2(unittest.TestCase):

    def test_no_palindrome_found(self):
        self.assertEqual(question2("1234568abc"), "")

    def test_palindrome_found(self):
        self.assertEqual(question2("abbaisgreat"), "abba")
        self.assertEqual(question2("abba2ablewasiereisawelba"), "ablewasiereisawelba")
        self.assertEqual(question2("24graba67b9"), "aba")
        self.assertEqual(question2("aa"), "aa")


