import unittest

class TestRearrange(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(rearrange([10,-1,20,4,5,-9,-6]), [-1,-9,-6,10,20,4,5])
        self.assertEqual(rearrange([0, 0, 0, -2]), [-2, 0, 0, 0])
        self.assertEqual(rearrange([-1, 2, -3, -4, 5]), [-1, -3, -4, 2, 5])

# Bubblesort?
def rearrange(lst: list) -> list:
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]

if __name__ == '__main__':
    unittest.main()
