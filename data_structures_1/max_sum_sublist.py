import unittest

class TestSumSublist(unittest.TestCase):
    def test_single(self):
        self.assertEqual(max_sum_sublist([-4, 2, -5, 1, 2, 3, 6, -5]), 12)

def max_sum_sublist(lst: list) -> int:

    global_max = lst[0]
    current_max = lst[0]
    
    for i in range(0, len(lst)):
        if current_max < 0:
            current_max = lst[i]
        else:
            current_max += lst[i]
        if global_max < current_max:
            global_max = current_max

    return global_max

if __name__ == '__main__':
    unittest.main()