import unittest

class TestRotateImage(unittest.TestCase):

    def test_9x9(self):
        input_matrix = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]]

        output_matrix = [[7, 4, 1], 
                         [8, 5, 2],
                         [9, 6, 3]]

        self.assertEqual(rotate_image(input_matrix), output_matrix)


def rotate_image(m):
    return m

if __name__ == '__main__':
    unittest.main()
