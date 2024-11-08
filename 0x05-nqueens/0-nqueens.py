#!/usr/bin/python3

import sys

def is_safe(board, col, row):
    """
    Checks if placing a queen at (row, col) is safe (doesn't attack any other queens).

    Args:
        board (list): List representing the chessboard (queen positions in each column).
        col (int): Current column.
        row (int): Row to check for queen placement.
    Returns:
            bool: True if placement is safe, False otherwise.
    """
    # Check for queens in the same row or diagonals
    for i in range(col):
        if board[i] == row or abs(col - i) == abs(row - board[i]):
            return False
    return True
def solve_n_queens(board, col):
    """
    Solves the N-Queens problem using backtracking algorithm.

    Args:
        board (list): List representing the chessboard (queen positions in each column).
        col (int): Current column to place the queen.
    Prints all possible solutions (queen positions) on the board.
    """
    if col == len(board):
        print(board)
        return
    for row in range(len(board)):
        if is_safe(board, col, row):
            board[col] = row
            solve_n_queens(board, col + 1)
            board[col] = -1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        exit(1)
    if N < 4:
        print("N must be at least 4", file=sys.stderr)
        exit(1)

    board = [-1] * N
    solve_n_queens(board, 0)
