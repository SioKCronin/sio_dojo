import unittest

input_list = [3, 9, 20, None, None, 15, 7]


class TestMinDepth(unittest.TestCase):
    def test_short(self):
        s = Solution()
        test = TreeNode(3)
        self.assertEqual(s.minDepth(test), 1)
        test.right = TreeNode(20)
        self.assertEqual(s.minDepth(test), 1)
        test.left = TreeNode(4)
        self.assertEqual(s.minDepth(test), 2)

    def test_shorter(self):
        s = Solution()
        test = TreeNode(1)
        test.left = TreeNode(2)
        self.assertEqual(s.minDepth(test), 2)

    def test_simple_tree(self):
        test = TreeNode(3)
        test.left = TreeNode(9)
        test.right = TreeNode(20)
        test.right.left = TreeNode(15)
        test.right.right = TreeNode(7)
        s = Solution()
        self.assertEqual(s.minDepth(test), 2)

    def test_longer_tree(self):
        test = TreeNode(3)
        test.left = TreeNode(9)
        test.right = TreeNode(20)
        test.left.left = TreeNode(4)
        test.left.right = TreeNode(5)
        test.right.left = TreeNode(15)
        test.right.right = TreeNode(7)
        s = Solution()
        self.assertEqual(s.minDepth(test), 3)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root, depth=0):
        if not root:
            return depth
        depth += 1
        return min(self.minDepth(root.left, depth), self.minDepth(root.right, depth))


if __name__ == "__main__":
    unittest.main()
