import math


def binary_search(sorted_list, target):

    length = len(sorted_list)

    if length == 0:
        print("Not here")
        return False

    if length == 1:
        if sorted_list[0] == target:
            print("Found it!")
            return True
        else:
            print("Not here")
            return False

    if length == 2:
        if sorted_list[0] == target or sorted_list[1] == target:
            print("Found it!")
            return True
        else:
            print("Not here")
            return False

    if length % 2 == 1:
        pivot = int(math.floor(length / 2))
        if target >= sorted_list[pivot]:
            return binary_search(sorted_list[pivot:], target)
        if target < sorted_list[pivot]:
            return binary_search(sorted_list[:pivot], target)
    else:
        pivot = int(length / 2)
        if target >= sorted_list[pivot]:
            return binary_search(sorted_list[pivot:], target)
        if target < sorted_list[pivot]:
            return binary_search(sorted_list[:pivot], target)

if __name__ == "__main__":
    print("Test continguous sorted")
    sorted_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    binary_search(sorted_list1, 11)
    #binary_search(sorted_list1, 4)
    #binary_search(sorted_list1, 10)

    print("Test non-continguous sorted")
    sorted_list2 = [1, 2, 5, 8, 10, 13]
    binary_search(sorted_list2, 4)

    print("Empty list")
    binary_search([], 4)

    print("Test all same number")
    binary_search([3, 3, 3, 3], 3)


