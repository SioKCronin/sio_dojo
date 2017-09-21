# Minion Game

'''
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 
'''
import unittest

def play(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevin_score = 0
    stuart_score = 0
    string_length = len(string)
    for i, letter in enumerate(string):
        if letter in vowels:
            kevin_score = kevin_score + string_length - i
        else:
            stuart_score = stuart_score + string_length - i

    if kevin_score < stuart_score:
        return 'Stuart {}'.format(stuart_score)
    elif kevin_score > stuart_score:
        return 'Kevin {}'.format(kevin_score)
    else:
        return 'Draw'

def minion_game(string):
    print(play(string))

class TestQuestion6(unittest.TestCase):
    def test_banana(self):
        string = 'BANANA'
        self.assertEqual(play(string), 'Stuart 12')

    def test_aaaaarkansas(self):
        string = 'AAAAARKANSAS'
        self.assertEqual(play(string), 'Kevin 57')

    def test_hard_string(self):
        string = "B"
        self.assertEqual(play(string), 'Stuart 1')

    def test_draw(self):
        self.assertEqual(play('BANANANAAAS'), 'Draw')
        self.assertEqual(play('BANAASA'), 'Draw')

if __name__ == '__main__':
    unittest.main()
