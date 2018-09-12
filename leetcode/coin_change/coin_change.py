import unittest
import time

class TestCoinChange(unittest.TestCase):

    def test_leet1(self):
        self.assertEqual(dp_coin_changer([1, 2, 5], 11, [0]*12), 3)
        self.assertEqual(dp_coin_changer([2], 3, [0]*4), -1)

def dp_coin_changer(coin_value_list, change, results):
    min_coins = change
    if change in coin_value_list:
        results[change] = 1
        return 1
    elif results[change] > 0:
        return results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + dp_coin_changer(coin_value_list, change-i, results)
            if num_coins < min_coins:
                min_coins = num_coins
                results[change] = min_coins
    if min_coins > len(coin_value_list):
        return -1
    return min_coins

if __name__ == '__main__':
    unittest.main()
