#!/usr/bin/python3
"""
pascal_triangle
"""

def pascal_triangle(n):
    """
    list of lists of integers representing the Pascal triangle of n
    """
    if n <= 0:
        return []

    pascal = []
    for i in range(n):
        base = [1]
        for j in range(i):
            
            base.append(sum(pascal[-1][j:j+2]))
        pascal.append(base)
    return pascal
