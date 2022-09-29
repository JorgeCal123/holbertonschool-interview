#!/usr/bin/python3
"""method island perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                #arriba
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                #izq
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                #der
                if j + 1 >= len(grid[i]) or grid[i][j + 1] == 0:
                    perimeter += 1
                #abajo
                if i + 1 >= len(grid) or grid[i + 1][j] == 0:
                    perimeter += 1

    return perimeter
