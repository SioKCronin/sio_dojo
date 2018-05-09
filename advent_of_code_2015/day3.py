# Day 3 - 2015

import numpy as np

m = np.zeros((1000, 1000))

with open('day3.txt') as f:
    data = f.read()

x = 500
y = 500

m[x][y] = 1

for char in data:
    if char == '^':
        y -= 1
    if char == 'v':
        y += 1
    if char == '<':
        x -= 1
    if char == '>':
        x += 1
    if m[x][y] == 0:
        m[x][y] = 1

total = sum([sum(i) for i in zip(*m)])

print(total)


