import unittest

class TestEditDistance(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(edit_distance("bee", "bear"), 2)

def edit_distance(x, y):

    n = max(len(x), len(y))
    add = 0
    mod = 0
    rem = 0

    def loop(x, y, add, mod, rem):
        # Define the base case of the recurrence 
        if len(x) > len(y):
            return [add, mod, rem]
        if len(x) < len(y):
            return [add, mod, rem]
        for i in range(n):
            add += 1 + loop(x[i:], y[i+1:], add, mod, rem)[0]
            mod += (x[0] != y[0]) + loop(x[i+1:], y[i+1:], add, mod, rem)[1]
            rem += 1 + loop(x[i+1:], y[i:], add, mod, rem)[2]
        print([add, mod, rem])

    loop(x, y, add, mod, rem)
    return min(add, mod, rem)

if __name__ == '__main__':
    unittest.main()

