# Interquartile Range

import unittest

def interquartile_range(n, x, f):

    strings = [str(y) for y in x]
    temp = [[y]*z for y,z in zip(strings,f)]
    s = [int(item) for sublist in temp for item in sublist]

    s = sorted(s)

    #Median
    if len(s) % 2 == 1:
        midpoint = (len(s) / 2) + 1
        q2 = float("{0:.1f}".format(s[((len(s) + 1)/2)-1]))
        l = s[:midpoint-1]
        u = s[midpoint:]
    else:
        midpoint = (len(s) / 2)
        q2 = float("{0:.1f}".format(((s[(len(s) / 2)-1]) + (s[(len(s)/ 2)])) / 2.0))
        l = s[:midpoint]
        u = s[midpoint:]

    #Q1
    if len(l) % 2 == 1:
        q1 = float("{0:.1f}".format(l[((len(l) + 1)/2)-1]))
    else:
        q1 = float("{0:.1f}".format(((l[(len(l)/2)-1]) + (l[(len(l)/2)])) / 2.0))

    #Q3
    if len(u) % 2 == 1:
        q3 = float("{0:.1f}".format(u[((len(u) + 1)/2)-1]))
    else:
        q3 = float("{0:.1f}".format(((u[(len(u)/2)-1]) + (u[(len(u)/2)])) / 2.0))

    print "l:", l
    print "u:", u
    print "s:", s
    print "q1:", q1
    print "q3:", q3

    return q3-q1

class TestInterquartileRange(unittest.TestCase):

    def test_sample_data(self):
        n = 6
        x = [6, 12, 8, 10, 20, 16]
        f = [5, 4, 3, 2, 1, 5]
        self.assertEqual(interquartile_range(n, x, f), 9.0)

if __name__ == '__main__':
    unittest.main()
'''
if __name__ == '__main__':
    n = int(raw_input())
    x = [int(y) for y in raw_input().split(" ")]
    f = [int(y) for y in raw_input().split(" ")]
    print interquartile_range(n, x, f))
'''
