import unittest

class TestHeaters(unittest.TestCase):

    def test_leet_example(self):
        self.assertEqual(heater_radius([1, 2, 3], [2]), 1)
        self.assertEqual(heater_radius([1, 2, 3, 4], [1,4]), 1)

def heater_radius(houses, heaters):
    tabs = [0 for x in houses]
    for i in range(tabs):
        tabs[i] = min([max([h - x for h in houses]) for x in heaters])

if __name__ == '__main__':
    unittest.main()
