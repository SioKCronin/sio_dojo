import unittest

class TestPangrams(unittest.TestCase):

    def test_pangram1(self):
        self.assertTrue(pangram1('the quick brown fox jumps over the lazy dog'))
        self.assertFalse(pangram1('the quick brown ox jumps over the lazy dog'))
        self.assertFalse(pangram1(''))

    def test_pangram2(self):
        self.assertTrue(pangram2('the quick brown fox jumps over the lazy dog'))
        self.assertFalse(pangram2('the quick brown ox jumps over the lazy dog'))
        self.assertFalse(pangram2(''))
        self.assertFalse(pangram2('a'))

    def test_pangram3(self):
        self.assertTrue(pangram3('the quick brown fox jumps over the lazy dog'))
        self.assertFalse(pangram3('the quick brown ox jumps over the lazy dog'))
        self.assertFalse(pangram3(''))
        self.assertFalse(pangram3('a'))

def pangram1(s):
    """Test equality of string set and alphabet set."""
    s = set(list(s.replace(" ","")))
    alphabet = set(map(chr, range(97, 123)))
    if s == alphabet:
        return True
    return False

def pangram2(s):
    """Sort list of string chars and compare to list of alphabet."""
    s = sorted(set(list(s.replace(" ",""))))
    alphabet = list(map(chr, range(97, 123)))
    if not bool(s):
        return False
    if len(s) != len(alphabet):
        return False
    for i, char in enumerate(alphabet):
        if char != s[i]:
            return False
    return True

def pangram3(s):
    """Evaluate symmetric difference of set of s and set of alphabet chars."""
    s = set(list(''.join(s.split())))
    alphabet = set(list(map(chr, range(97, 123))))
    return not bool(s.symmetric_difference(alphabet))

if __name__ == '__main__':
    unittest.main()
