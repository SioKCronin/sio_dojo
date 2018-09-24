import unittest

class TestAddTwoNumbers(unittest.TestCase):

    def test_leet_example(self):
        class ListNode(object):
            def __init__(self, x):
                self.val = x
                self.next = None
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        target = ListNode(7)
        target.next = ListNode(0)
        target.next.next = ListNode(8)
        self.assertEqual(addTwoNumbers(l1, l2), target)

def addTwoNumbers(l1, l2):
    first = []
    second = []
    node1 = l1
    node2 = l2
    while node1:
        first.append(str(node1.val))
        node1 = node1.next
    while node2:
        second.append(str(node2.val))
        node2 = node2.next
    first.reverse()
    second.reverse()
    s = str(int("".join(first)) + int("".join(second)))
    output = [x for x in s]
    output.reverse()
    start_node = output[0]
    node = start_node
    for i in output[1:]:
        output[i] = ListNode(reversed_output[i])
        node.next = output[i]
        node = reversed_output[i]
    return start_node

if __name__ == '__main__':
    unittest.main()
