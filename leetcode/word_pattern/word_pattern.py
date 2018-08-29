import unittest

class TestWordPattern(unittest.TestCase):

    def test_leet_example(self):
        self.assertTrue(word_pattern('abba', 'dog cat cat dog'))
        self.assertFalse(word_pattern('abba', 'dog cat cat fish'))
        self.assertFalse(word_pattern('aaaa', 'dog cat cat dog'))
        self.assertFalse(word_pattern('abba', 'dog dog dog dog'))

def word_pattern(pattern, s):
    words = s.split()
    first = words[0]
    second = None
    decoded_pattern = "a"
    for word in words[1:]:
        if word == first:
            decoded_pattern += 'a'
        elif word != first and second == None:
            second = word
            decoded_pattern += 'b'
        elif word == second:
            decoded_pattern += 'b'
        else:
            decoded_pattern += 'x'
    if pattern == decoded_pattern:
        return True
    return False

if __name__ == '__main__':
    unittest.main()
