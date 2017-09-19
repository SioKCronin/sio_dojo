# Standard Deviation

import unittest

def std_deviation(n, array):
    # Mean
    mean = float("{0:.1f}".format(sum(array)/ float(n)))
    squares = []
    for x in array:
        squares.append((x-mean)**2)
    return float("{0:.1f}".format((sum(squares)/float(n))**.5print "{}\n{}\n{}".format(*mean_median_mode(n, array))print "{}\n{}\n{}".format(*mean_median_mode(n, array))))

class TestStdDeviation(unittest.TestCase):

    def test_sample_array(self):
        n = 5
        array = [10, 40, 30, 50, 20]
        self.assertEqual(std_deviation(n, array), 14.1)

    def test_decimal_examples(self):
        n = 6
        array = [10.1, 40.4, 30.3, 50.5, 20.2]
        self.assertEqual(std_deviation(n, array))

if __name__ == '__main__':
    unittest.main()
'''
if __name__ == '__main__':
    # unittest.main()
    n = int(raw_input())
    array = [int(x) for x in raw_input().split(" ")]
    print std_deviation(n, array)
'''
