import unittest
import asyncio

class StackUsingQueue():

    def __init__(self):
        self.stack = asyncio.LifoQueue()

class TestStackUsingQueue(unittest.TestCase):

    def test_setup(self):
        self.assertIsInstance(s, StackUsingQueue)

