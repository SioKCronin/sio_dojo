import unittest

class TestFindFirstUnique(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_first_unique([1,2,2,3,3]), 1)

def find_first_unique(l: list) -> int:
    for val in l:
        if l.count(val) == 1:
            return val

if __name__ == '__main__':
    unittest.main()