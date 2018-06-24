import unittest

two_board = [[0, 0], [0, 0]]

three_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

class TestNQueens(unittest.TestCase):
    def test_2_by_2(self):
        self.assertFalse(n_queens(two_board, 2))

    def test_3_by_3(self):
        self.assertTrue(n_queens(three_board, 3))

def is_attacked(x, y, board, N):
    # Column attack
    for i in range(N):
        if board[i][x] == 1:
            return True

    # Row attack
    for j in range(N):
        if board[y][j] == 1:
            return True

    # Diagonal attack
    for i in range(N):
        for j in range(N):
            if i+j == x+y and board[i][j] == 1:
                return True
            if i-j == x-y and board[i][j] == 1:
                return True

def n_queens(board, N):
    if N == 0:
        return True
    for i in range(N):
        for j in range(N):
            if is_attacked(i, j, board, N):
                continue
            board[i][j] = 1
            if n_queens(board, N-1):
                return True
            board[i][j] = 0
    return False

if __name__ == '__main__':
    unittest.main()
