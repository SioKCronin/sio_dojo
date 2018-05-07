# Day 1 - 2015

def transform_data(data):
    return [x for x in data.strip().split()]

with open('day1.txt') as f:
    data = transform_data(f.read())

for x in data:
    base = 0
    i = 1
    for char in x:
        if char == '(':
            base += 1
        if char == ')':
            base -= 1
        if base < 0:
            print(i)
            break
        i += 1
    print(base)


