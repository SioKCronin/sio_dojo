import unittest

class TestNiceStrings(unittest.TestCase):

    def test_contains_three_vowels(self):
        self.assertTrue(contains_three_vowels('aei'))
        self.assertTrue(contains_three_vowels('aeiaeiaei'))
        self.assertTrue(contains_three_vowels('aexi'))
        self.assertFalse(contains_three_vowels('xxx'))
        self.assertFalse(contains_three_vowels(''))
        self.assertFalse(contains_three_vowels('ai'))

    def test_contains_double_letters(self):
        self.assertTrue(contains_doubles('xx'))
        self.assertTrue(contains_doubles('abcddef'))
        self.assertTrue(contains_doubles('aaaabb'))
        self.assertFalse(contains_doubles(''))
        self.assertFalse(contains_doubles('xax'))

    def test_contains_forbidden_pairs(self):
        self.assertTrue(contains_forbidden_pairs('cabc'))
        self.assertTrue(contains_forbidden_pairs('cdcdcd'))
        self.assertFalse(contains_forbidden_pairs('xxxxxx'))
        self.assertFalse(contains_forbidden_pairs(''))

    def test_is_nice(self):
        self.assertTrue(is_nice('ugknbfddgicrmopn'))
        self.assertTrue(is_nice('aaa'))
        self.assertFalse(is_nice('jchzalrnumimnmhp'))
        self.assertFalse(is_nice('haegwjzuvuyypxyu'))

def contains_three_vowels(s):
    if sum([1 for c in s if c in 'aeiou']) >= 3:
        return True
    return False

def contains_doubles(s):
    prev = None
    for c in s:
        if c == prev:
            return True
        prev = c
    return False

def contains_forbidden_pairs(s):
    pairs = [''.join(i) for i in zip(s, s[1:])]

    for pair in pairs:
        if pair in ['ab', 'cd', 'pq', 'xy']:
            return True
    return False

def is_nice(s):
    if contains_three_vowels(s) and contains_doubles(s) and not contains_forbidden_pairs(s):
        return True
    return False

if __name__ == '__main__':
    def transform_data(data):
        return [x for x in data.strip().split()]

    with open('day5.txt') as f:
        data = transform_data(f.read())

    total = 0
    for row in data:
        if is_nice(row):
            total += 1
    print(total)
    # unittest.main()
