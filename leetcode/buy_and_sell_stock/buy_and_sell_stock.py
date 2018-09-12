import unittest

class TestStock(unittest.TestCase):

    def test_leet_examples(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)
        self.assertEqual(max_profit([1, 2]), 1)

    def test_2(self):
        self.assertEqual(max_profit2([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit2([7, 6, 4, 3, 1]), 0)
        self.assertEqual(max_profit2([1, 2]), 1)

    def test_3(self):
        self.assertEqual(max_profit3([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(max_profit3([7, 6, 4, 3, 1]), 0)
        self.assertEqual(max_profit3([1, 2]), 1)

def max_profit(prices):
    best = 0
    if len(prices) <= 1:
        return best
    else:
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > best:
                    best = prices[j] - prices[i]
        return best

def max_profit2(prices):
    best = 0
    if len(prices) <= 1:
        return best
    else:
        for i in range(len(prices)):
            if max(prices[i:]) - prices[i] > best:
                best = max(prices[i:]) - prices[i]
    return best

def max_profit3(prices):
    if len(prices) <= 1:
        return 0
    low = prices[0]
    best = 0
    for value in prices:
        if value < low:
            low = value
        profit = value - low
        if profit > best:
            best = profit
    return best

if __name__ == '__main__':
    unittest.main()
