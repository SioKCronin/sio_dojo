import unittest

class TestEditDistance(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(edit_distance("bee", "bear"), 2)
        self.assertEqual(edit_distance("horse", "ros"), 3)
        self.assertEqual(edit_distance("intention", "execution"), 5)

def edit_distance(x, y):

    n = max(len(x), len(y))
    add = 0
    mod = 0
    rem = 0

    def loop(x, y, add, mod, rem):
        if (not x) or (not y):
            return min(add + abs(len(x)-len(y)), mod, rem)
        if len(x) == 1 and len(y) == 1:
            if x == y:
                return min(add, mod, rem)
            return min(add, mod + 1, rem)

        for i in range(n-1):
            add += 1 + loop(x[i:], y[i+1:], add, mod, rem)
            mod += (x[0] != y[0]) + loop(x[i+1:], y[i+1:], add, mod, rem)
            rem += 1 + loop(x[i+1:], y[i:], add, mod, rem)

    return loop(x, y, add, mod, rem)

if __name__ == '__main__':
    unittest.main()

