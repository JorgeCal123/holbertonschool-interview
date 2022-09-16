#!/usr/bin/python3
"""
rotates 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
    rotate a matrix
    """
    rotate = list(zip(*matrix[::-1]))
    i = len(matrix)
    j = len(matrix[0])
    for v in range(i):
        for e in range(j):
            matrix[v][e] = rotate[v][e]
    return matrix
