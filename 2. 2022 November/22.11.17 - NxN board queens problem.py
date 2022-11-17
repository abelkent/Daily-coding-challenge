"""
You have an N by N board. 

Write a function that, given N, returns the number of possible arrangements 
of the board where N queens can be placed on the board without threatening each other,
i.e. no two queens share the same row, column, or diagonal.
"""

def N_queens_problem(N):

    board = [[False] * N] * N
    print(board)
    print(board[0])

N_queens_problem(3)