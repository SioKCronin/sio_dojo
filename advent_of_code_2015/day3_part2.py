# Day 3 Part 2 - 2015

import numpy as np

m = np.zeros((1000, 1000))

with open('day3.txt') as f:
    data = f.read()

x = [500,500]
y = [500,500]

m[500][500] = 1

toggle = True

counter = 0

for char in data:
    if toggle:
        idx = 0
    else:
        idx = 1
    if char == '^':
        y[idx] -= 1
    if char == 'v':
        y[idx] += 1
    if char == '<':
        x[idx] -= 1
    if char == '>':
        x[idx] += 1
    x_coord = x[idx]
    y_coord = y[idx]
    if m[x_coord][y_coord] == 0:
        santa_x, santa_y  = x[0],y[0]
        robo_x, robo_y  = x[1], y[1]
        m[santa_x][santa_y] = 1
        m[robo_x][robo_y] = 1
    toggle = not toggle

total = sum([sum(i) for i in zip(*m)])

print(total)
