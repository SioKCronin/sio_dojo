# Day 3 - part2
import pandas as pd
from collections import deque

def transform_data(data):
    return [int(x) for x in data.strip().split()]

with open('day3.txt') as f:
    transform = transform_data(f.read())
    data = [transform[i:i+3] for i in range(0, len(transform), 3)]

sample_data = [[101, 301, 501],
               [102, 302, 502],
               [103, 303, 503],
               [201, 401, 601],
               [202, 402, 602],
               [203, 403, 603]]

df = pd.DataFrame(data=data)
transposed = df.T
rows = transposed.values.tolist()
data = []

for row in rows:
    while row:
        one = row.pop(0)
        two = row.pop(0)
        three = row.pop(0)
        data.append((one, two, three))

count = 0

for trio in data:
    print(trio)
    if (trio[0] + trio[1] > trio[2]) and \
       (trio[1] + trio[2] > trio[0]) and \
       (trio[0] + trio[2] > trio[1]):
       count += 1

print(count)
