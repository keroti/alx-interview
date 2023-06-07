#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise
    and don't return anything but matrix in place
    """
    n = len(matrix)

    # Rotate the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row of the rotated matrix
    for i in range(n):
        matrix[i] = matrix[i][::-1]
