import unittest

graph = [3, 9, 20, None, None, 15, 7]

class TestPathSum(unittest.TestCase):

    def test_simple(self):
        test = TreeNode(3)
        test.left = TreeNode(5)
        self.assertTrue(path_sum(test, 8))

    def test_simple(self):
        test = TreeNode(3)
        test.left = TreeNode(5)
        self.assertFalse(path_sum(test, 3))

    def test_simple(self):
        test = TreeNode(1)
        test.left = TreeNode(2)
        test.left.left = TreeNode(3)
        test.left.left.left = TreeNode(4)
        test.left.left.left.left = TreeNode(5)
        self.assertFalse(path_sum(test, 3))

    def test_leet_examples(self):
        test = TreeNode(3)
        test.left = TreeNode(9)
        test.right = TreeNode(20)
        test.right.left = TreeNode(15)
        test.right.right = TreeNode(7)
        self.assertFalse(path_sum(test, 22))

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def path_sum(node, target, s=0):

    if not node:
        return s
    else:
        s += node.val
    if path_sum(node.left


    '''
    if not node:
        if s == target:
            return True
        return False
    else:
        s += node.val
        return path_sum(node.left, target, s) or path_sum(node.right, target, s)
    '''

if __name__ == '__main__':
    unittest.main()
