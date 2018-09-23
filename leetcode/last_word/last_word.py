import unittest

class TestLastWord(unittest.TestCase):

    def test_leet_example(self):
        self.assertEqual(last_word_length("Hello World"), 5)
        self.assertEqual(last_word_length(""), 0)
        self.assertEqual(last_word_length("a "), 1)

def last_word_length(s):
    s.strip()
    words = s.split()
    if not words:
        return 0
    else:
        return len(words[-1])

if __name__ == '__main__':
    unittest.main()
