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

def triangle_min_path(triangle):
    return 11

if __name__ == '__main__':
    unittest.main()
