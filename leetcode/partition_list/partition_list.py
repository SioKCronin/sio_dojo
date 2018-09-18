import unittest

class TestPartitionList(unittest.TestCase):

    def test_leet_example(self):
        head = ListNode(1)
        four = ListNode(4)
        three = ListNode(3)
        two = ListNode(2)
        five = ListNode(5)
        two2 = ListNode(2)
        head.next = four
        four.next = three
        three.next = two
        two.next = five
        five.next = two2
        s = Solution(head, 5)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

if __name__ == '__main__':
    unittest.main()
