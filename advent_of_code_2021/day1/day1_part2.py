# Day 1 - 2021 

import numpy as np
import operator

def transform_data(data):
    return [x for x in data.strip().split()]

def sum_sliding_window(data):
    return [int(data[x]) + int(data[x+1]) + int(data[x+2]) for x in range(0, len(data)-2)]

with open('day1.txt') as f:
    data = transform_data(f.read())

def depth_counter(data):

    data = sum_sliding_window(data)

    print(data)
    #print(len(data))

    counter = 0
    
    for x in range(1, len(data)):
        # print((data[x-1], data[x]))
        if data[x] > data[x-1]:
            #print((data[x-1], data[x]))
            counter += 1

    return counter

print(depth_counter(data))
