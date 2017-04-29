# Day 1

import numpy as np

def transform_data(data):
    return [(x[0], int(x[1:])) for x in data.strip().split(', ')]

def next_direction(current_direction, instruction):
    return {
        'N': {'R': 'E', 'L': 'W'},
        'S': {'R': 'W', 'L': 'E'},
        'E': {'R': 'S', 'L': 'N'},
        'W': {'R': 'N', 'L': 'S'}
    }[current_direction][instruction]

def blocks_from_instructions(instructions):
    dirs = {
        'N': np.array([0, 1]),
        'S': np.array([0, -1]),
        'E': np.array([1, 0]),
        'W': np.array([-1, 0])
    }
    coords = np.array([0, 0])
    current_direction = 'N'
    for instruction in instructions:
        current_direction = next_direction(current_direction, instruction[0]) 
        coords = coords + (dirs[current_direction] * instruction[1])
    return abs(coords[0]) + abs(coords[1])

with open('day1.txt') as f:
    data = transform_data(f.read())

# print blocks_from_instructions([('R',2),('L',3)])
# print blocks_from_instructions([('R', 2), ('R', 2), ('R', 2)])

print blocks_from_instructions(data)

