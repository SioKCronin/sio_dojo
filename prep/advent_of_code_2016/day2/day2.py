# Day 2

def transform_data(data):
    return [x for x in data.strip().split()]

# with open('day2_test.txt') as f:
#    data = transform_data(f.read())

with open('day2.txt') as f:
    data = transform_data(f.read())

def index_increment(direction, y_id, x_id):
    if direction == 'U':
        if y_id == 0:
            y_id = y_id
        else:
            y_id -= 1
    if direction == 'D':
        if y_id == 2:
            y_id = y_id
        else:
            y_id += 1
    if direction == 'R':
        if x_id == 2:
            x_id = x_id
        else:
            x_id += 1
    if direction == 'L':
        if x_id == 0:
            x_id = x_id
        else:
            x_id -= 1
    return y_id, x_id

y_id = 1
x_id = 1

table = [[ 1, 2, 3], [ 4, 5, 6], [ 7, 8, 9]]
code = []

for line in data:
    for x in line:
        y_id, x_id = index_increment(x, y_id, x_id)
    code.append(table[y_id][x_id])

answer = ''.join(str(e) for e in code)

print(answer)
