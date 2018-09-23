import unittest

class TestAddBinary(unittest.TestCase):

    def test_leet_example1(self):
        self.assertEqual(add_binary("11", "1"), "100")
        self.assertEqual(add_binary("1010", "1011"), "10101")

def add_binary(a, b):
    a = int(a, 2)
    b = int(b, 2)
    s = a+b
    return format(s, 'b')

if __name__ == '__main__':
    unittest.main()
