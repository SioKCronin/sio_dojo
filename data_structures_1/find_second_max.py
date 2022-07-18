import unittest

class TestSecondMax(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_second_max([1, 2, 3, 4]), 3)

def find_second_max(lst: list) -> int:
    lst.sort()
    max_val = lst[-1]
    for val in reversed(lst):
        if val != max_val:
            return val

if __name__ == '__main__':
    unittest.main()