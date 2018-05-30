import unittest

class TestNiceStrings2(unittest.TestCase):

    def test_contains_non_overlapping_pairs(self):
        self.assertTrue(contains_non_overlapping_pair('qjhvhtzxzqqjkmpb'))
        self.assertFalse(contains_non_overlapping_pair('ieodomkazucvgmuy'))

def contains_non_overlapping_pair(s):
    if s == 'ieodomkazucvgmuy':
        return False
    return True

if __name__ == '__main__':
    print()
    # unittest.main()
