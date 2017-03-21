# Question 2
'''
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
'''
import unittest

def find_center(a):
    '''
    Generate x and y for all palindrome centers.
    If center is made up of two adjescent equivalent characters,x = y
    '''
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            yield i-1, i
        if i+1 < len(a) and a[i-1] == a[i+1]:
            yield i, i

def palindrome_is_expandable(string, left, right):
    return left >= 0 \
        and right < len(string) \
        and string[left] == string[right]

def build_palindrome(string, left, right):
    '''
    Build palindrome accepts the string and the first and and last index of the center,
    which for cases of a single center index, will be the same current.
    This function builds up the longest substring palindrome possible around the center provided.
    '''
    i = 0
    while palindrome_is_expandable(string, left - i, right + i):
        palindrome = string[left - i: right + i + 1]
        i +=1
    return palindrome

def question2(a):
    '''
    Return longest possible substring palindrome.
    '''
    longest_palindrome = ""
    for x, y in find_center(a):
         current = build_palindrome(a, x, y)
         if len(current) > len(longest_palindrome):
             longest_palindrome = current
    return longest_palindrome

class TestQuestion2(unittest.TestCase):

    def test_no_palindrome_found(self):
        self.assertEqual(question2("1234568abc"), "")

    def test_two_character_palindrome_found(self):
        self.assertEqual(question2("cc"), "cc")
        self.assertEqual(question2("a13cc2"), "cc")

    def test_three_character_palindorom_found(self):
        self.assertEqual(question2("aba"), "aba")
        self.assertEqual(question2("231abaab1a"), "baab")

    def test_longer_than_three_chars_palindrome_found(self):
        self.assertEqual(question2("abccba"), "abccba")
        self.assertEqual(question2("abcba"), "abcba")

    def test_find_center(self):
        self.assertEqual(list(find_center("abba")), [(1,2)])
        self.assertEqual(list(find_center("cc")), [(0, 1)])
        self.assertEqual(list(find_center("abbaabbaa")), [(1, 2), (3, 4), (5, 6), (7, 8)])

    def test_embedded_overlappling_palindromes(self):
        self.assertEqual(question2("abbaabbaa"), "abbaabba")

if __name__ == '__main__':
    unittest.main()

