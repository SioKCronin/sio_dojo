import unittest

class TestPangrams(unittest.TestCase):

    def test_pangram1(self):
        self.assertTrue(pangram1('the quick brown fox jumps over the lazy dog'))
        self.assertTrue(pangram1('the quick brown fox jumps over the lazy dog lazy dog'))
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

"""PANGRAM 1
I wanted to be able to compare my string to the chars in the alphabet, 
so I decided to create a list of each. The choice of using set was motivated
by a desire to remove duplicates, as I just needed to find at least one of each
char in the alphabet. At most, 26 pairs of chars will be evaluated with '=='.
I thought I could get away with O(1) if I joined the sets as strings, but
the equality comparison would still be over 26 chars, not the 1 string. 

    Runtime: O(1 + 1 + 26) --> O(26)
    Space: O(1 + 1) --> O(1)
"""

def pangram1(s):
    """Test equality of string set and alphabet set."""
    s = set(list(s.replace(" ","")))
    alphabet = set(map(chr, range(97, 123)))
    if s == alphabet:
        return True
    return False

"""PANGRAM 2
I wanted to see if there was another way to break as soon as we knew two chars 
were different, which essentially just makes visible what is happening in the 
set equality check of function 1.

    Runtime: O(n + 26) --> O(n)
    Space: O(1 + 1 + 1 + 1 + n) --> O(n)

"""

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

"""PANGRAM 3
This exploits the symmetric_difference method of sets, which will evaluate
as True if it contains an element, and False if it is the empty set. 

    Runtime: O(n + 26) --> O(n)
    Space: O(1 + 1) --> O(1)

"""

def pangram3(s):
    """Evaluate symmetric difference of set of s and set of alphabet chars."""
    s = set(list(''.join(s.split())))
    alphabet = set(list(map(chr, range(97, 123))))
    return not bool(s.symmetric_difference(alphabet))

if __name__ == '__main__':
    unittest.main()
