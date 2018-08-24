import unittest

class TestSymmetricTree(unittest.TestCase):

    def test_is_mirror(self):
        self.assertTrue(check_symmetry([1, 2, 2, 3, 4, 4, 3]))
        self.assertFalse(check_symmetry([1, 2, 2, null, 3, null, 3]))

def check_symmetry(root):
    left_root = root
    right_root = root
    left = []
    right = []
    while True:
        if left_root:
            left.append(left_root.left)
        left_root = left_root.left

    while True:
        if right_root:
            right.append(right_root.right)
        right_root = right_root.right

if __name__ == '__main__':
    unittest.main()





