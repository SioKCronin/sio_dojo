import unittest

class TestRerverseVowels(unittest.TestClass):

    def test_leet_examples(self):
        self.assertEqual(reverse_vowels("hello"), "holle")
        self.assertEqual(reverse_vowels("leetcode"), "leotcede")

def reverse_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    letters = list(s)
    last_vowel = []

    for i, letter in enumerate(letters):
        if letter in vowels:

        if (letter in vowels) and vowel_stack and (letter != vowel_stack[-1]):
            swap = vowel_stack.pop()
            letters[i] = swap
            vowel_stack.append(letter)

        else:
            vowel_stack.append(letter)

    return ''.join(letters)
