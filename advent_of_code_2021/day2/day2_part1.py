# Day 2 - 2021

def transform_data(data):
    return [x.strip().split() for x in data.strip().splitlines()]

with open("day2.txt") as f:
    data = transform_data(f.read())

def depth_traversed(data):
    hor = 0
    vert = 0

    for x in range(0, len(data)):
        if data[x][0] == 'forward':
            hor += int(data[x][1])
        elif data[x][0] == 'down':
            vert += int(data[x][1])
        else:
            vert -= int(data[x][1])

    space_traversed = hor * vert

    return space_traversed

print(depth_traversed(data))
