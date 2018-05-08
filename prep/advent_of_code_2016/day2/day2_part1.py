def transform_data(data):
    return [x for x in data.strip().split()]

with open('day2.txt') as f:
    data = transform_data(f.read())

def increment_idx(direction, coords):
    coords = coords
    directions = {'U':[0, 0,-1],
                  'D':[0, 2, 1],
                  'R':[1, 2, 1],
                  'L':[1, 0,-1]}

    if directions[direction][0] == 0:
        if coords[0] == directions[direction][1]:
            pass
        else:
            coords[0] += directions[direction][2]
    else:
        if coords[1] == directions[direction][1]:
            pass
        else:
            coords[1] += directions[direction][2]
    return coords

coords = [1, 1]
table = [[ 1, 2, 3], [ 4, 5, 6], [ 7, 8, 9]]
code = []

for line in data:
    for character in line:
        coords = increment_idx(character, coords)
    code.append(table[coords[0]][coords[1]])

answer = ''.join(str(e) for e in code)

print(answer)
