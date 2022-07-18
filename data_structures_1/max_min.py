import unittest

class TestMaxMin(unittest.TestCase):

    def test_single(self):
        self.assertEqual(max_min([1,2,3,4,5]), [5,1,4,2,3])

def max_min(lst: list) -> list:

    # Option 1

    # make a new list of length list you were given with 'x'
    # iterate over your new list
    # make tail_index(-1) and head_index(0)
    # iterate over new list
    # if i % 2 == 0 then set value[i] = lst[head_index]
    # else value[i] = lst[tail_index]
    # increment whichever you set

    # Swap option
    # 0 and -1
    # 1 and -1
    # 2 and -1

    # Option 2

    # reversed_or_not = -1 or 1
    # new_list = []

    # while len(lst) > 1:
    # if -1:
    # reversed(list)
    # new_list.append(list[0])
    # reversed_or_not = reversed_or_not * -1
    # procede with list[1:]

    #Option 3
     # insert_index (increment by 2)
    # 
    # incrememt your index
    # repeat

    index = 0

    while len(lst) > index + 1:
        lst.insert(index, lst[-1])
        lst = lst[:-1]
        index += 2
    return lst

if __name__ == '__main__':
    unittest.main()