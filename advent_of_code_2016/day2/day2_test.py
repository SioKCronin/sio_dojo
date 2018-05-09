# Day 2 test

from day2 import find_code

code = []

for x in data:
    code.append(find_code(x))

answer = ''.join(str(e) for e in code)

if answer != 1985:
    print("Sorry, try again")
