import unittest

class TestPascalsTriangle2(unittest.TestCase):

    def test_leet_example(self):
        self.assertEqual(pascals_kth_row(3), [1, 3, 3, 1])
        self.assertEqual(pascals_kth_row(2), [1, 2, 1])
        self.assertEqual(pascals_kth_row(4), [1, 4, 6, 4, 1])

def pascals_kth_row(k):
    if k == 0: return [1]
    if k == 1: return [1, 1]
    else:
        array = [1, 1]
        for i in range(k-1):
            inner = []
            for j in range(1, len(array)):
                inner.append(array[j] + array[j-1])
            array = [1] + inner + [1]
    return array

if __name__ == '__main__':
    unittest.main()
