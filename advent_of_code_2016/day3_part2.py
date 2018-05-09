# Day 3 - part2
import pandas as pd

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

df = pd.DataFrame(data=sample_data)
iters = df.T.shape[1]

# Just slice them off in threes and then move to the next column. Done.

count = 0

for trio in data:
    print(trio)
    if (trio[0] + trio[1] > trio[2]) and \
       (trio[1] + trio[2] > trio[0]) and \
       (trio[0] + trio[2] > trio[1]):
       count += 1

print(count)
