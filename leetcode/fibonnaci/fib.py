def fib_iter(n):
    if n <= 1:
        return n
    total = 0
    first = 0
    second = 1
    for i in range(n):
        return fib_iter(n-1) + fib_iter(n-2)

def fib_recur(n):
    if n <= 1:
        return n
    return fib_recur(n-1) + fib_recur(n-2)

def fib_dp(n):
    memo = {0:0, 1:1}
    for i in range(n):
        if i not in n:
            memo[i] = fib_dp(n-1) + fib_dp(n-2)
        return memo[i]
