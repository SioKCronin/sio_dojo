import unittest

class TestRemoveEvens(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(remove_even([1, 2, 3, 4]),[1, 3])
        self.assertEqual(remove_even([1, 2, 3, 4, 0, -41, -40]),[1, 3, 0, -41])

def remove_even(l: list) -> list:
    for val in l:
        if val % 2 == 0:
            l.remove(val)
    return l

if __name__ == '__main__':
    unittest.main()