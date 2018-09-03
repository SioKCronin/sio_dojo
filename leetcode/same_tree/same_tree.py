import unittest

class TestSameTree(unittest.TestCase):

    def test_leet_examples(self):
        self.assertTrue(same_tree_checker([1,2,3], [1,2,3]))
        self.assertFalse(same_tree_checker([1,2], [1, None,2]))
        self.assertFalse(same_tree_checker([1,2,1], [1,1,2]))

def same_tree_checker(tree1, tree2):
    return True

if __name__ == '__main__':
    unittest.main()
