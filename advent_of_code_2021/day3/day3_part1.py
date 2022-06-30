# Day 3 - Part 1

def transform_data(data):
    return [x for x in data.strip().splitlines()]

with open("day3.txt") as f:
    data = transform_data(f.read())

def derive_rates(data):

    one = [0 for x in range(0, 12)]
    zero = [0 for x in range(0, 12)]

    for x in range(0, len(data)):
        for y in range(0, 12):
            if data[x][y] == '1':
                zero[y] += 1
            else:
                one[y] += 1

    # Gamma Rates

    gamma_array = [0 for x in range(0, 12)]

    for y in range(0, 12):
        if one[y] > zero[y]:
            gamma_array[y] = 1

    gamma_string = ''.join([str(i) for i in gamma_array])
    gamma_rate = int(gamma_string, 2)

    # Epsilon Rates

    epsilon_array = [0 for x in range(0, 12)]

    for y in range(0, 12):
        if gamma_array[y] == 0:
            epsilon_array[y] = 1

    epsilon_string = ''.join([str(i) for i in epsilon_array])    
    epsilon_rate = int(epsilon_string, 2)

    power_consumption = gamma_rate * epsilon_rate

    return power_consumption

print(derive_rates(data))
