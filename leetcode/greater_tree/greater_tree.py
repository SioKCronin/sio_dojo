while node or stack:
    while node:
        stack.append(node)

        node = node.right
    node = stack.pop()
    temp_value = node.val
    node.val += x
    x += temp_value
    node = node.left

'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13
          / \
         1   4

Output: The root of a Greater Tree like this:
                 (5+13)
              /                             \
          2+(5+13)+ 4                        13 + 0
         /                 \
   1 +(2+5+13) + 4  4 + (5 + 13)
   
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def convertBST(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    stack = [root]
    running_sum = 0

    def build_stack(stack):
      while stack:
        node = stack.pop(0)
        if node.right:
          stack.append(root.right)

class Solution:
    def __init__(self):
        self.sums = 0
        
    def convertBST(self,root):
        if not root:
            return None
        self.convertBST(root.right)
        temp_value = root.val
        root.val += self.sums
        self.sums += temp_value
        self.convertBST(root.left)
        return root
      
def convertBST2(root, x = [0]):
	if not root:
		return None
	convertBST2(root.right,x)
	temp_value = root.val
	root.val += x[0]
	x[0] += temp_value
	convertBST2(root.left,x)
	return root

class Solution:
    def convertBST(self, root):
        return convertBST2(root, x = [0])

class Solution:
    def convertBST(self,root):
        x = 0
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node)

                node = node.right
            node = stack.pop()
            temp_value = node.val
            node.val += x
            x += temp_value
            node = node.left

        return root

