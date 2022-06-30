# Day 2 - 2021

def transform_data(data):
    return [x.strip().split() for x in data.strip().splitlines()]

with open("day2.txt") as f:
    data = transform_data(f.read())

def depth_traversed(data):
    aim = 0
    horizontal = 0
    depth = 0

    for x in range(0, len(data)):
        if data[x][0] == 'forward':
            horizontal += int(data[x][1])
            depth += int(data[x][1]) * aim
        elif data[x][0] == 'down':
            # depth += int(data[x][1])
            aim += int(data[x][1])
        else:
            # depth -= int(data[x][1])
            aim -= int(data[x][1])

    return horizontal * depth

print(depth_traversed(data))
