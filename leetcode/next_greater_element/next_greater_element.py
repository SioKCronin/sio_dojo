import unittest

class TestNextGreater(unittest.TestCase):

    def test_my_example(self):
        self.assertEqual(next_greater([1, 2], [2, 1]), [2, -1])

    def test_leet_examples(self):
        self.assertEqual(next_greater([4, 1, 2], [1, 3, 4, 2]), [-1, 3, -1])
        self.assertEqual(next_greater([2, 4], [1, 2, 3, 4]), [3, -1])

def next_greater(l1, l2):
    output = []
    for i, num in enumerate(l1):
        for j, second_num in l2:
            if num = second_num:
                flag = True
                for test in l2[j:]:
                    if test > second_num:
                        output.append(test)
                        flag = False
                        break
        if flag:
            output.append(-1)
    return output

if __name__ == '__main__':
    unittest.main()
