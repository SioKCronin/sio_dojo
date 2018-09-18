import unittest

class TestUniquePaths(unittest.TestCase):

    def test_leet_example(self):
        self.assertEqual(unique_paths(3, 2, 0, 0), 3)
        self.assertEqual(unique_paths(7, 3, 0, 0), 28)

def unique_paths(m, n, i, j):

    if i > m or j > n:
        return 0

    if i == m and j == n:
        return 1

    return unique_paths(m, n, i+1, j) + unique_paths(m, n, i, j+1)

if __name__ == '__main__':
    unittest.main()
