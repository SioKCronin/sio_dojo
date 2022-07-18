import unittest
import copy

class TestFindProduct(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_product([1,2,3,4]), [24,12,8,6])

def find_product(l: list) -> list:
    result = []
    for val in l:
        sum = 1
        c = copy.copy(l)
        c.remove(val)
        for i in range(len(c)):
            sum = sum * c[i]
        result.append(sum)
    return result

if __name__ == '__main__':
    unittest.main()