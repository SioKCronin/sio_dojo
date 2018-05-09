# Mean Median Mode

import unittest

def mean_median_mode(n, array):
    # Mean
    mean = float("{0:.1f}".format(sum(array)/ float(n)))

    #Median
    array = sorted(array)
    if len(array) % 2 == 1:
        midpoint = len(array) / 2
        median = float("{0:.1f}".format(array[((len(array) + 1)/2)-1]))
    else:
        median = float("{0:.1f}".format(((array[(len(array)/2)-1]) + (array[(len(array)/2)])) / 2.0))

    #Mode
    counter = 0
    value = 0
    for x in array:
        if array.count(x) > counter:
            counter = array.count(x)
            value = x
    mode = value

    return [mean, median, mode]

class TestMeanMedianMode(unittest.TestCase):

    def test_simple_array(self):
        n = 5
        array = [10, 20, 30, 40, 50]
        self.assertEqual(mean_median_mode(n, array), [30.0, 30.0, 10.0])

    def test_another_simple_array(self):
        n = 5
        array = [20, 30, 40, 50, 60]
        self.assertEqual(mean_median_mode(n, array), [40.0, 40.0, 20.0])

    def test_long_decimels(self):
        n = 3
        array = [13.245666, 10.1, 11.78888]
        self.assertEqual(mean_median_mode(n, array),[11.7, 11.8, 10.1])

    def test_failed_example(self):
        n = 10
        array = [64630, 11735, 14216, 99233, 14470, 4978, 73429, 38120, 51135, 67060]
        self.assertEqual(mean_median_mode(n, array), [43900.6, 44627.5, 4978])

'''
if __name__ == '__main__':
    unittest.main()
'''

if __name__ == '__main__':
    # unittest.main()
    n = int(raw_input())
    array = [int(x) for x in raw_input().split(" ")]
    print "{}\n{}\n{}".format(*mean_median_mode(n, array))
