# Day 1 - 2021 

import numpy as np
import operator

def transform_data(data):
    return [x for x in data.strip().split()]

with open('day1.txt') as f:
    data = transform_data(f.read())

def depth_counter(data):

    #print(data)
    #print(len(data))

    counter = 0
    
    for x in range(1, len(data)):
        # print((data[x-1], data[x]))
        if data[x] > data[x-1]:
            #print((data[x-1], data[x]))
            counter += 1

    return counter

print(depth_counter(data))
