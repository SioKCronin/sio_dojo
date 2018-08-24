import unittest

class TestWordPattern(unittest.TestCase):

    def test_leet_example(self):
        self.assertTrue(word_pattern('abba', 'dog cat cat dog'))
        self.assertFalse(word_pattern('abba', 'dog cat cat fish'))
        #self.assertFalse(word_pattern('aaaa', 'dog cat cat dog'))
        #self.assertFalse(word_pattern('abba', 'dog dog dog dog'))

def word_pattern(pattern, s):
    return True

if __name__ == '__main__':
    unittest.main()
