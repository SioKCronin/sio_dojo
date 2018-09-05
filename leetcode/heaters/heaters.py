import unittest

class TestHeaters(unittest.TestCase):

    def test_leet_examples(self):
        self.assertEqual(heater_radius([1, 2, 3], [2]), 1)
        self.assertEqual(heater_radius([1, 2, 3, 4], [1,4]), 1)

    def test_my_examples(self):
        self.assertEqual(heater_radius([1, 2, 3, 4, 5], [2]), 3)
        self.assertEqual(heater_radius([1, 2, 3, 4], [1,4]), 1)

def heater_radius(houses, heaters):
    output = [list() for i in range(len(houses))]
    for heater in heaters:
        for i, house in enumerate(houses):
            output[i].append(abs(house - heater)) 
    return max([min(x) for x in output])

if __name__ == '__main__':
    unittest.main()
