import unittest

class TestFindMin(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_min([1,2,3,4]), 1)

def find_min(l: list) -> int:
    least = l[0]
    for val in l:
        if val < least:
            least = val
    return least

if __name__ == '__main__':
    unittest.main()
