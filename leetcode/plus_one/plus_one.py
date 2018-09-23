import unittest

class TestPlusOne(unittest.TestCase):

    def test_leet_example1(self):
        self.assertEqual(plus_one([1, 2, 3]), [1, 2, 4])
        self.assertEqual(plus_one([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertEqual(plus_one([9]), [1, 0])

def plus_one(digits):
    return [int(x) for x in str(int(''.join(str(i) for i in digits)) + 1)]

if __name__ == '__main__':
    unittest.main()
