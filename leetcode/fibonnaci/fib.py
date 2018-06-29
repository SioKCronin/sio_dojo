import unittest

class TestFibs(unittest.TestCase):

    def test_fib_iter(self):
        self.assertEqual(fib_iter(3), 2)

    def test_fib_recur(self):
        self.assertEqual(fib_recur(3), 2)

    def test_fib_recur(self):
        self.assertEqual(fib_dp(3), 2)

    def test_fib_space_efficient(self):
        self.assertEqual(fib_space_efficient(3), 2)

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
    def _fib_dp(n):
        if n not in memo:
            memo[n] = _fib_dp(n-1) + _fib_dp(n-2)
        return memo[n]
    return _fib_dp(n)

def fib_space_efficient(n):
    if n == 0:
        return 0

    back2 = 0
    back1 = 1

    for i in range(2,n):
        next_val = back1 + back2
        back2 = back1
        back1 = next_val

    return(back1+back2)

if __name__ == '__main__':
    unittest.main()
