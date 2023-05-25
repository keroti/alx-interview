#!/usr/bin/python3
"""
N queens problem
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check for queens in the lower diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, solutions):
    """
    Solve the N queens problem using backtracking
    """
    # Base case: all queens are placed
    if row == len(board):
        solutions.append(board[:])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place the queen
            board[row][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens(board, row + 1, solutions)

            # Backtrack and remove the queen
            board[row][col] = 0


def print_solutions(solutions):
    """
    Print the solutions in the required format
    """
    for solution in solutions:
        print([[i, j] for i, j in enumerate(solution)])


if __name__ == '__main__':
    # Validate and parse the command-line argument
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize an empty chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N queens problem
    solutions = []
    solve_nqueens(board, 0, solutions)

    # Print the solutions
    print_solutions(solutions)
