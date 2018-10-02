def square_of_sum(count):
    return sum([i for i in range(1, count+1)])**2

def sum_of_squares(count):
    return sum([i**2 for i in range(1, count+1)])

def difference(count):
    return abs(sum_of_squares(count) - square_of_sum(count))
