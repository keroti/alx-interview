#!/usr/bin/python3
""" FUNCTION FOR PASCAL'S TRIANGLE """


def pascal_triangle(n):
    """
    Pascal's triangle
    Args:
      n (int): The number of rows in the triangle
    Returns:
      List of lists of integers for the triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
