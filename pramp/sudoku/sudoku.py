'''
Write the function sudokuSolve that checks whether a given sudoku board (i.e. sudoku puzzle) 
is solvable. If so, the function will returns true. Otherwise (i.e. there 
is no valid solution to the given sudoku board), returns false.

The key insights are we can create a helper function that generates valid ints
for a given position (finding the valid ints that remain after removing what 
is already present in row, column and subgroup), and iterate through these 
to see if we can solve the board were we to select that value. If not, we
backtrack and try again. 

An important element is the checking valid in the subgroup. 
'''
import unittest
import copy
import math

class TestSudokuSolver(unittest.TestCase):

    def test_pramp_example(self):
        board = [[5, 3, '.', '.', 7, '.', '.', '.', '.'],
                 [6, '.', '.', 1, 9, 5, '.', '.', '.'],
                 ['.', 9, 8, '.', '.', '.', '.', 6, '.'],
                 [8, '.', '.', '.', 6, '.', '.', '.', 3],
                 [4, '.', '.', 8, '.', 3, '.', '.', 1],
                 [7, '.', '.', '.', 2, '.', '.', '.', 6],
                 ['.', 6, '.', '.', '.', '.', 2, 8, '.'],
                 ['.', '.', '.', 4, 1, 9, '.', '.', 5],
                 ['.', '.', '.', '.', 8, '.', '.', 7, 9]
                ]
        self.assertTrue(sudoku_solver(board))

def sudoku_solver(board):

    def valid_board(board):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    return False
        return True

    def valid_ints(board, row, col):
        valid_ints = []

        for c in list(range(1, 10)):
            collision = False
            for i in range(9):
                if (board[row][i] == c or
                    board[i][col] == c or
                    board[(row - row % 3) + math.floor(i / 3)][(col - col % 3) + i % 3] == c):
                        collision = True 
                        break
                if not collision:
                    valid_ints.append(c)
        return valid_ints

    if valid_board(board):
        return True
    else:
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    board2 = copy.copy(board)
                    valids = valid_ints(board, i, j)
                    for val in valids:
                        board2[i][j] = val
                        if sudoku_solver(board2):
                            return True
                        else:
                            board2[i][j] = '.'
    return False

if __name__ == '__main__':
    unittest.main()
