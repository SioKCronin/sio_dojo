import unittest

input = "the sky is blue"

class TestRerverseWords(unittest.TestCase):

    def test_leet_example(self):
        self.assertEqual(reverse_words("the sky is blue"), "blue is sky the")

    def test_leading_spaces(self):
        self.assertEqual(reverse_words("   the sky is blue"), "blue is sky the")

    def test_intersticial_spaces(self):
        self.assertEqual(reverse_words("the   sky is blue"), "blue is sky the")

def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    unittest.main()
