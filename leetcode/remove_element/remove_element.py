import unittest

class TestRemoveElement(unittest.TestCase):

    def test_leet_examples(self):
        self.assertEqual(remove_element([3, 2, 2, 3], 3), [2, 2])
        self.assertEqual(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2), [0, 1, 3, 0, 4])

def remove_element(nums, val):
    # return [x for x in nums if x != val]

    #for i, num in enumerate(nums):
    #    if num == val:
    #        nums[i] = None
    #return list(filter(lambda x: x!=None, nums))

    # Just removes the first occurance
    #nums.remove(val)

    i = 0

    while i < len(nums)-1:
        if i < 0:
            i = 0
            continue
        for i, num in enumerate(nums):
            if num == val:
                del nums[i]
                i -= 1
                break

    return nums

if __name__ == '__main__':
    unittest.main()
