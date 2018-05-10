# Day 4 - Part 2

from collections import Counter
import string

def transform_data(data):
    return [x for x in data.strip().split()]

with open('day4.txt') as f:
    data = transform_data(f.read())

def quantify_name(fixed, checksum):
    return True

test = 'qzmt-zixmtkozy-ivhz-343'
example = [char for char in test]
code = []
sectorID_sum = 343

#for char in example:
#    if char == '-':
#        code.append(' ')
#    else:
#        if (ord(char) + (sectorID_sum%26)) > 122:
#            code.append(chr(97 + ((ord(char) + (sectorID_sum%26))-123)))
#        else:
#            code.append(chr((ord(char) + (sectorID_sum%26))))
#code = ''.join(char for char in code)
#final_code = code.split(' ')
#if 'presents' in final_code or 'toys' in final_code:
#    print(sectorID_sum)
##print(final_code)

sectorID_sum = 0

def checksum(line):
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
    return (fixed2 == checksum)


for line in data:
    parts = line.split('[')
    if checksum(line):
        code = []
        for char in parts[0][:-4]:
            if char == '-':
                code.append(' ')
            else:
                if (ord(char) + (sectorID_sum%26)) > 122:
                    code.append(chr(97 + ((ord(char) + (sectorID_sum%26))-123)))
                else:
                    code.append(chr((ord(char) + (sectorID_sum%26))))
        code = ''.join(char for char in code)
        final_code = code.split(' ')
        print(final_code)
