#!/usr/bin/python3
"""" Module for island_perimeter. """


def island_perimeter(grid):
    """
    Function that returns the perimeter of the island described in grid.
    """
    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])

    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == 1:
                perimeter += 4  # Each land cell contributes 4 sides to perimeter

                # Check adjacent cells and subtract shared sides
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Subtract top side
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Subtract left side

    return perimeter
