import unittest

class TestRightRotate(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(right_rotate([10,20,30,40,50], 3), [30,40,50,10,20])

def right_rotate(lst: list, k: int) -> list:

    result = ['x' for i in range(len(lst))]

    for i, val in enumerate(lst):
        if i + k >= len(lst):
            index = k + i - len(lst)
            result[index] = val
        else:
            index = k + i
            result[index] = val

    return result

if __name__ == '__main__':
    unittest.main()