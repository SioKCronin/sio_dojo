# Day 2-Part2 - 2015

def transform_data(data):
    return [[y for y in x.strip().split('x')] for x in data.strip().split()]

with open('day2.txt') as f:
    data = transform_data(f.read())

total_ribbon = 0

for present in data:
    l = int(present[0])
    w = int(present[1])
    h = int(present[2])
    bow = l*w*h
    smallest_sides = [l, w, h]
    smallest_sides.sort()
    two_sides = smallest_sides[:2]
    total_ribbon += (2*two_sides[0]) + (2*two_sides[1]) + bow

print(total_ribbon)

