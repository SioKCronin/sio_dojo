# Day 2 part 2

def transform_data(data):
    return [x for x in data.strip().split()]

with open('day2.txt') as f:
    data = transform_data(f.read())

def increment_idx(direction, coords):
    coords = coords
    if direction == 'U':
        if coords[0] == 0 or table[coords[0]-1][coords[1]] == 0:
            pass
        else:
            coords[0] += -1
    if direction == 'D':
        if coords[0] == 4 or table[coords[0]+1][coords[1]] == 0:
            pass
        else:
            coords[0] += 1
    if direction == 'R':
        if coords[1] == 4 or table[coords[0]][coords[1]+1] == 0:
            pass
        else:
            coords[1] += 1
    if direction == 'L':
        if coords[1] == 0 or table[coords[0]][coords[1]-1] == 0:
            pass
        else:
            coords[1] += -1
    return coords

coords = [2, 0]
y_id = 2
x_id = 0

table = [[ 0, 0, 1, 0, 0],
         [ 0, 2, 3, 4, 0],
         [ 5, 6, 7, 8, 9],
         [ 0,'A','B','C', 0],
         [ 0, 0, 'D',0, 0]]
code = []

for line in data:
    for character in line:
        coords = increment_idx(character, coords)
    code.append(table[coords[0]][coords[1]])

answer = ''.join(str(e) for e in code)

print(answer)
