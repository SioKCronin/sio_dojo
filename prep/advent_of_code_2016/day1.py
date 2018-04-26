# Day 1

import numpy as np
import operator

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
    historic_coords = np.array([0,0])
    current_direction = 'N'
    for instruction in instructions:
        current_direction = next_direction(current_direction, instruction[0]) 
        coords = coords + (dirs[current_direction] * instruction[1])
    return abs(coords[0]) + abs(coords[1])

with open('day1.txt') as f:
    data = transform_data(f.read())

def visited_twice(instructions):
    dirs = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
    }

    span = {
        'N': (0, 0),
        'S': (0, 0),
        'E': (0, 0),
        'W': (0, 0)
    }

    coords = (0,0)
    current_direction = 'N'
    historic_coords = []
    for instruction in instructions:
        current_direction = next_direction(current_direction, instruction[0])
        coords = tuple(map(operator.add, coords,
            tuple([z * instruction[1] for z in dirs[current_direction]])))
        y = tuple([z * instruction[1] for z in dirs[current_direction]])
        #print(tuple([z * instruction[1] for z in dirs[current_direction]]))
        print(coords)
        if coords in historic_coords:
            return abs(coords[0]) + abs(coords[1])
        historic_coords.append(coords)
        # It seems we should keep track of everywhere we've passed through
        # If anything is in the span, then include it
        # How do we keep track of intersections?

# print blocks_from_instructions([('R',2),('L',3)])
# print blocks_from_instructions([('R', 2), ('R', 2), ('R', 2)])
# print blocks_from_instructions(data)
print(visited_twice(data))
