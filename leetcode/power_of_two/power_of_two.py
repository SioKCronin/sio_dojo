import unittest

class TestPowerOfTwo(unittest.TestCase):

    def test_leet_examples(self):
        self.assertTrue(power_of_two(1))
        self.assertTrue(power_of_two(2))
        self.assertTrue(power_of_two(16))
        self.assertFalse(power_of_two(218))

def power_of_two(num):
    if num == 1: return True
    if num == 2: return True
    if num < 1: return False
    else:
        return power_of_two(num /2)

if __name__ == '__main__':
    unittest.main()
