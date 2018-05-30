import unittest

class TestNiceStrings2(unittest.TestCase):

    def test_contains_non_overlapping_pairs(self):
        self.assertTrue(contains_non_overlapping_pair('qjhvhtzxzqqjkmpb'))
        self.assertTrue(contains_non_overlapping_pair('xyxy'))
        self.assertTrue(contains_non_overlapping_pair('aaabaa'))
        self.assertFalse(contains_non_overlapping_pair('ieodomkazucvgmuy'))
        self.assertFalse(contains_non_overlapping_pair('aaa'))

    def test_letter_pairs_with_one_between(self):
        self.assertTrue(letter_pairs_with_one_between('xox'))
        self.assertTrue(letter_pairs_with_one_between('aabacd'))
        self.assertTrue(letter_pairs_with_one_between('abcdeaba'))
        self.assertFalse(letter_pairs_with_one_between('abcde'))

def contains_non_overlapping_pairs(s):
    # Won't it only overlap if the two letters are the same?
    pairs = [''.join(i) for i in zip(s, s[1:])]

    for i, pair in enumerate(pairs):
        if pair in pairs[i+2:]:
            return True
    return False

def letter_pairs_with_one_between(s):
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            return True
    return False

def is_nice(s):
    if contains_non_overlapping_pairs(s) and letter_pairs_with_one_between(s):
        return True
    return False

if __name__ == '__main__':
    with open('day5.txt') as f:
        print(sum([is_nice(s) for s in f]))
    # unittest.main()
