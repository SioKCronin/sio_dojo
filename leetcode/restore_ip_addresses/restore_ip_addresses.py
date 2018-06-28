import unittest

class TestIPAddressRestorer(unittest.TestCase):

    def test_all_ones(self):
        self.assertEqual(ipRestorer("11111111111"), ["11.111.111.111",
                                                     "111.11.111.111",
                                                     "111.111.11.111",
                                                     "111.111.111.11"]

def ipRestorer(s):

    partials = []

