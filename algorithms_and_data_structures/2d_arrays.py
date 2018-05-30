# 2D Arrays

import numpy as np

def sum_hourglasses(matrix):
    sums = []
    for i in range(0,4):
        for j in range(0,4):
            value = (matrix[i][j] +  
                    matrix[i][j+1] + 
                    matrix[i][j+2] + 
                    matrix[i+1][j+1] + 
                    matrix[i+2][j] + 
                    matrix[i+2][j+1] + 
                    matrix[i+2][j+2])
            sums.append(value)

    # There has to be three rows below 
    # Top left index must be less or equal to len(row) - 3

    return max(sums)

# Import the data into a matrix
count = 0
data = []
while count < 6:
    data.append([int(i) for i in raw_input().strip().split(' ')])
    count += 1

# Call function with imported data

print sum_hourglasses(data)



