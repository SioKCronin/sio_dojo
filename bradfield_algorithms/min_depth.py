import unittest

input_list = [3,9,20,'null','null',15,7]

real_input = [None if i == "null" else i for i in input_list]

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

l = []

class Solution(object):
    def minDepth(self, root, depth=0):
        if root:
            self.minDepth(root.left, depth +1)
            self.minDepth(root.right, depth +1)
        else:
            l.append(depth)
 
        return min(l)        preorder(tree.right)

test = TreeNode(real_input[0])
test.left = TreeNode(real_input[1])
test.right = TreeNode(real_input[2])
test.left.left = TreeNode(real_input[3])
test.left.right = TreeNode(real_input[4])
test.right.left = TreeNode(real_input[5])
test.right.right = TreeNode(real_input[6])

if __name__ == '__main__':
    unittest.main()
