#!/bin/python3
#!/bin/python3

import sys

def search_and_add(a, b, k):
    while a != b+1:
        base_list[a] = base_list[a] + k
        a = a + 1

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    
    base_list = [0 for i in list(range(n))]
    
    big_list = []
    top = 0
    
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a)-1, int(b)-1, int(k)]
        
        new_list = [0 for i in list(range(a))] + [k for i in list(range((b+1) - a))] + [0 for i in list(range(n-b-1))]
        big_list.append(new_list)
        
    for i in list(range(n)):
        for w in list(range(m)):
        
    while n != 0:
        base_list = map(add, base_list, new_list)
        
    print(max(base_list))
