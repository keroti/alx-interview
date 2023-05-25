#!/usr/bin/python3
"""
N queens problem
"""
import sys


def first_board(n):
    """
    Initialize a 2 by 2 sized chessboard.
    """
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_copy(board):
    """
    Return a copy of a chessboard.
    """
    if isinstance(board, list):
        return list(map(board_copy, board))
    return (board)


def solution(board):
    """
    Return the list of lists representation of a solved chessboard
    """
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "Q":
                solution.append([i, j])
                break
    return (solution)


def spots(board, row, col):
    """
    Remove spots queen can no longer pklay
    """
    # forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def solve(board, row, queens, solutions):
    """
    Solve an N-queens puzzle and return solution
    """
    if queens == len(board):
        solutions.append(solution(board))
        return (solutions)

    for i in range(len(board)):
        if board[row][i] == " ":
            new_board = board_copy(board)
            new_board[row][i] = "Q"
            spots(new_board, row, i)
            solutions = solve(new_board, row + 1,
                              queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = first_board(int(sys.argv[1]))
    solutions = solve(board, 0, 0, [])
    for solve in solutions:
        print(solve)
