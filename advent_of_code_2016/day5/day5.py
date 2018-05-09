# Day 5

# Look at haslib and binascii

import binascii

# MD5 hash - take the 6th if first 5 are zeros in hexadecimal

n = 8
door_id = []

def generate_hex(index):
    data = b'uqwqemis'
    return binascii.hexlify(data)

for i in range(n):
    index = 0
    while generate_hex(index)[:5] != '00000':
        index += 1
    door_id.append(generate_hex(data, index)[6])

print(''.join(str(e) for e in door_id))


