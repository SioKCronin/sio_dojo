# Day 3

def transform_data(data):
    return [int(x) for x in data.strip().split()]

with open('day3.txt') as f:
    transform = transform_data(f.read())
    data = [transform[i:i+3] for i in range(0, len(transform), 3)]

#with open('day3_test.txt') as f:
#    transform = transform_data(f.read())
#    data = [transform[i:i+3] for i in range(0, len(transform), 3)]

count = 0

for trio in data:
    print(trio)
    if (trio[0] + trio[1] > trio[2]) and (trio[1] + trio[2] > trio[0]) and (trio[0] + trio[2] > trio[1]):
        count += 1

print(count)
