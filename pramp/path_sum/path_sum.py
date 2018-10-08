'''
Find the minimal Sales Path cost in a tree.
'''
import unittest

class TestSalesPath(unittest.TestCase):

    def test_simple_case(self):
        rootNode = Node(5)
        one = Node(1)
        two = Node(2)
        one.parent = rootNode
        two.parent = rootNode
        rootNode.children.append(one)
        rootNode.children.append(two)
        self.assertEqual(get_cheapest_cost(rootNode), 6)

class Node:

  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None

def get_cheapest_cost(rootNode, path_sum = 0):
  if not rootNode or not rootNode.children:
    return path_sum
  else:
    path_sum += rootNode.cost
    return min([get_cheapest_cost(child, path_sum + child.cost) for child in rootNode.children])
    
'''
function getCheapestCost(rootNode):
    n = len(rootNode.children)

    if (n == 0):
        return rootNode.cost
    else:
        # initialize minCost to the largest integer in the system
        minCost = MAX_INT
        for i from 0 to n-1:
            tempCost = getCheapestCost(rootNode.child[i])
            if (tempCost < minCost):
                minCost = tempCost

    return minCost + rootNode.cost

'''

if __name__ == '__main__':
    unittest.main()
