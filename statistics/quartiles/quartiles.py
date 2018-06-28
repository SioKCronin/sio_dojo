import unittest

def quartile(n, array):

    array = sorted(array)

    #Q2
    if n % 2 == 1:
        midpoint = (n / 2) + 1
        q2 = float("{0:.1f}".format(array[((n + 1)/2)-1]))
        l = array[:midpoint-1]
        u = array[midpoint:]
    else:
        midpoint = (n / 2)
        q2 = float("{0:.1f}".format(((array[(n / 2)-1]) + (array[(n / 2)])) / 2.0))
        l = array[:midpoint]
        u = array[midpoint:]

    #Q1
    if len(l) % 2 == 1:
        q1 = float("{0:.1f}".format(l[((len(l) + 1)/2)-1]))
    else:
        q1 = float("{0:.1f}".format(((array[(len(l)/2)-1]) + (array[(len(l)/2)])) / 2.0))

    #Q3
    if len(u) % 2 == 1:
        q3 = float("{0:.1f}".format(u[((len(u) + 1)/2)-1]))
    else:
        q3 = float("{0:.1f}".format(((u[(len(u)/2)-1]) + (u[(len(u)/2)])) / 2.0))

    return [q1, q2, q3]

class TestQuartlies(unittest.TestCase):

    def test_short_array(self):
        n = 9
        array = [3, 7, 8, 5, 12, 14, 21, 13, 18]
        self.assertEqual(quartile(n, array), [6, 12, 16])

    def test_odd_array(self):
        n = 5
        array = [1, 2, 3, 4, 5]
        self.assertEqual(quartile(n, array), [1.5, 3, 4.5])

    def test_even_array(self):
        n = 4
        array = [2, 4, 6, 8]
        self.assertEqual(quartile(n, array), [3, 5, 7])
'''
if __name__ == '__main__':
    unittest.main()
'''
if __name__ == '__main__':
    n = int(raw_input())
    array = [int(x) for x in raw_input().split(" ")]
    print "{}\n{}\n{}".format(*quartile(n, array))
