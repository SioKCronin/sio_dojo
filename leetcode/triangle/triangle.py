import unittest

class TestTriangle(unittest.TestCase):

    def test_example1(self):
        triangle = [    [2],
                      [3, 4], 
                    [6, 5, 7], 
                   [4, 1, 8, 3]
                   ]
        self.assertEqual(triangle_min_path(triangle), 11)

    def test_example2(self):
        triangle = [    [2],
                      [3, 4], 
                    [6, 1, 7], 
                   [4, 1, 8, 3]
                   ]
        self.assertEqual(triangle_min_path(triangle), 7)

    def test_example2(self):
        triangle = [    [-1],
                       [2, 3],
                     [1, -1,-3]
                   ]
        self.assertEqual(dp_triangle_min_path(triangle), -1)

def triangle_min_path(t):
    if not t: return 0
    if len(t) == 1: return t[0][0]

    best = t[0][0]
    loc = 0
    for layer in t[1:]:
        if layer[loc] <= layer[loc +1]:
            best += layer[loc]
        else:
            best += layer[loc+1]
            loc += 1
    return best

def dp_triangle_min_path(t):
    if not t: return 0
    if len(t) == 1: return t[0][0]

    memo = [[0]*len(x) for x in t]
    memo[0][0] = t[0][0]

    for i in range(1, len(t)):
        for j in range(len(t[i])):
            if j == 0:
                memo[i][j] = memo[i-1][j] + t[i][j]
            elif j == len(t[i]) - 1:
                memo[i][j] = memo[i-1][j-1] + t[i][j]
            else:
                memo[i][j] += min(memo[i-1][j], memo[i-1][j-1]) + t[i][j]
        print(memo)

    return min(memo[-1])

if __name__ == '__main__':
    unittest.main()
