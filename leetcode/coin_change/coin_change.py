import unittest
import time

class TestCoinChange(unittest.TestCase):

    def test_leet1(self):
        self.assertEqual(dp_coin_changer([1, 2, 5], 11, [0]*12), 3)
        self.assertEqual(dp_coin_changer([2], 3, [0]*4), -1)

def inefficeint_coin_changer(coin_value_list, amount):
    min_coins = amount
    if amount in coin_value_list:
        return 1
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + inefficient_coin_changer(coin_value_list, change-i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

def dp_coin_changer(coinValueList, change, results):
    minCoins = change
    if change in coinValueList:
        results[change] = 1
        return 1
    elif results[change] > 0:
        return results[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + dp_coin_changer(coinValueList, change-i, results)
            if numCoins < minCoins:
                minCoins = numCoins
                results[change] = minCoins
    if minCoins > len(coinValueList):
        return -1
    return minCoins

if __name__ == '__main__':
    unittest.main()
