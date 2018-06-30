import unittest

class TestEditDistance(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(edit_distance("bee", "bear"), 2)
        self.assertEqual(edit_distance("horse", "ros"), 3)
        self.assertEqual(edit_distance("intention", "execution"), 5)

def edit_distance(x, y):

    n = max(len(x), len(y))
    memo = []

    def loop(x, y):
        if (not x) and (not y):
            #print("Found empties")
            return 0

        if (not x) or (not y):
            #print("Found one empty")
            return abs(len(x)-len(y))

        if len(x) == 1 and len(y) == 1:
            #print("Found single lists")
            if x == y:
                return 0
            return 1

        for i in range(n-1):
            add = 1 + loop(x[i:], y[i+1:])
            mod = (x[0] != y[0]) + loop(x[i+1:], y[i+1:])
            rem = 1 + loop(x[i+1:], y[i:])
            #memo.append(min(add, mod, rem))
            return min(add, mod, rem)

    return loop(x, y)
    #loop(x, y)
    #return sum(memo)

if __name__ == '__main__':
    unittest.main()

