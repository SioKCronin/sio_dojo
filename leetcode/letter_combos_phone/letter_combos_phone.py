import unittest
import itertools

class TestLetterCombos(unittest.TestCase):

    def test_leet_examples(self):

        self.assertEqual(letter_combos("23"),["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]) 

def letter_combos(s):
    letters = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z'], 
               '0': [],
               '1': []}

    if not s: return []

    if len(s) == 1:
        return letters[s]

    memo = letters[s[:1]]

    return [x + y for x, y in itertools.product(memo, letter_combos(s[1:]))] 

if __name__ == '__main__':
    unittest.main()
