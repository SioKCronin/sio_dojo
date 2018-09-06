import unittest

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TestSameTree(unittest.TestCase):

    def test_leet_example1(self):
        t1 = TreeNode(1)
        t1.left = TreeNode(2)
        t1.right = TreeNode(3)
        t2 = TreeNode(1)
        t2.left = TreeNode(2)
        t2.right = TreeNode(3)
        self.assertTrue(equal_trees(t1, t2))

    def test_leet_example2(self):
        t1 = TreeNode(1)
        t1.left = TreeNode(2)
        t2 = TreeNode(1)
        t2.right = TreeNode(2)
        self.assertFalse(equal_trees(t1, t2))

def equal_trees(p, q):
    if (not p and not q):
        return True

    if (not p and q) or (not q and p):
        return False

    if p.val != q.val:
        return False

    return (equal_trees(p.left, q.left) or equal_trees(p.right, q.right))

if __name__ == '__main__':
    unittest.main()
