import unittest

class QueueUsingStack():

    def __init__(self):
        self.queue = []

    def push(self, x):
        return self.queue.append(x)

    def pop(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def empty(self):
        return self.queue == []

class TestQueueUsingStack(unittest.TestCase):

    def test_queue_setup(self):
        q = QueueUsingStack()
        self.assertIsInstance(q, QueueUsingStack)

    def test_push(self):
        q = QueueUsingStack()
        q.push(2)
        self.assertEqual(q.queue, [2])

    def test_pop(self):
        q = QueueUsingStack()
        q.push(2)
        q.push(3)
        self.assertEqual(q.pop(), 2)

    def test_peek(self):
        q = QueueUsingStack()
        q.push(2)
        q.push(3)
        self.assertEqual(q.peek(), 2)

    def test_empty(self):
        q = QueueUsingStack()
        q.push(2)
        q.push(3)
        self.assertFalse(q.empty())

if __name__ == '__main__':
    unittest.main()
