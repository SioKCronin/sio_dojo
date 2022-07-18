import unittest

class TestContainsDuplicate(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(containsDuplicate([1, 2, 2, 3]))

def containsDuplicate(l):

    s = set()

    for x in l:
        if x in s:
            return True
        else:
            s.add(x)


if __name__ == '__main__':
    unittest.main()