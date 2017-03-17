# Question 5

import unittest

'''
Find the element in a singly linked list that's m elements from the end.
For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element.
The function definition should look like question5(ll, m), where ll is the first node of a linked
list and m is the "mth number from the end". You should copy/paste the Node class below to use as a
representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
'''

class Node(object):
  def __init__(self, data, next_node = None):
    self.data = data
    self.next = next_node

def question5(ll, m):
    values = [ll.data]
    while ll.next:
        ll = ll.next
        values.append(ll.data)
    return  values[0-m]

class TestQuestion5(unittest.TestCase):

    def test_one_node(self):
        linked_list = Node(5)
        self.assertEqual(question5(linked_list, 1), 5)

    def test_five_nodes(self):
        n = None
        for i in reversed(range(1,6)):
            current = Node(i, n)
            n = current
        self.assertEqual(question5(n, 3), 3)
        self.assertEqual(question5(n, 4), 2)
        self.assertEqual(question5(n, 1), 5)

if __name__ == '__main__':
    unittest.main()

