import unittest

class TestMaxSubarray(unittest.TestCase):

    def test_example(self):
        self.assertEqual(max_subarray([-2,1,-3,4,-1,2,1,-5,4]),6)
        self.assertEqual(max_subarray([1]), 1)
        self.assertEqual(max_subarray([1, 2]), 3)

    def test_negatives(self):
        self.assertEqual(max_subarray([-1]), -1)
        self.assertEqual(max_subarray([-2,-1]), -1)
        self.assertEqual(max_subarray([-2,-3, -1]), -1)

def max_subarray(l):
    best = min(l)
    memo = 0

    for i in range(len(l)):
        memo = max(l[i], memo +l[i])
        best = max(best, memo)

    return best

    #N = len(l)
    #memo = []
    # My O(N^2) version
    #for i in range(N-1):
    #    for j in range(i+1,N+1):
    #        memo.append(sum(l[i:j]))
    #memo.append(l[-1])
    #return max(memo)

if __name__ == '__main__':
    unittest.main()

