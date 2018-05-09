# Day 4

from collections import Counter

def transform_data(data):
    return [x for x in data.strip().split()]

with open('day4.txt') as f:
    data = transform_data(f.read())

def quantify_name(fixed, checksum):
    return True

sectorID_sum = 0

for line in data:
    parts = line.split('[')
    code = []
    checksum = parts[1].strip(']')
    for char in parts[0]:
        if char != '-':
            code.append(char)
    values = code[-3:]
    room_id = code[:-3]
    room_val = ''.join(str(e) for e in values)
    a = sorted(Counter(room_id).most_common(), key=lambda item: (-item[1], item[0]))
    fixed2 = ''.join(str(e[0]) for e in a[:5])
    if fixed2 == checksum:
        sectorID_sum += int(room_val)

print(sectorID_sum)
