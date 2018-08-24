import unittest

class TestSymmetricTree(unittest.TestCase):

    def test_is_mirror(self):
        test = TreeNode(1)
        test.left = TreeNode(2)
        test.right = TreeNode(2)
        test.right.left = TreeNode(3)
        test.right.right = TreeNode(4)
        test.right.left = TreeNode(4)
        test.right.right = TreeNode(3)
        self.assertTrue(check_symmetry(test))

    def test_not_mirror(self):
        test = TreeNode(1)
        test.left = TreeNode(2)
        test.right = TreeNode(2)
        test.right.left = TreeNode(None)
        test.right.right = TreeNode(3)
        test.right.left = TreeNode(None)
        test.right.right = TreeNode(3)
        self.assertFalse(check_symmetry(test))

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def check_symmetry(root):
    if root:
        check_symmetry(root.left)
        check_symmetry(root.right)
    else:
        return True

if __name__ == '__main__':
    unittest.main()
