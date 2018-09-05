import unittest

graph = [3, 9, 20, None, None, 15, 7]

class TestPathSum(unittest.TestCase):

    def test_leet_examples(self):
        test = TreeNode(3)
        test.left = TreeNode(9)
        test.right = TreeNode(20)
        test.right.left = TreeNode(15)
        test.right.right = TreeNode(7)
        s = Solution()
        self.assertTrue(s.generate_path_sum(test, 22, 3))

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generate_path_sum(graph, target, vertex, path=[], s=0):
        print("graph", graph)
        print("vertex", vertex)
        s += vertex
        path += [vertex]
        if not graph[vertex] and target == s:
            return path
        elif graph[vertex]:
            for child in graph[vertex]:
                generate_path_sum(graph, child, path, s)
        return None

if __name__ == '__main__':
    unittest.main()
