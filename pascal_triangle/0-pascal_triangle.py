#!/usr/bin/python3

import math

"""returns a list of lists of integers representing the Pascal's triangle"""

def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n rows."""
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        row = [math.comb(i, j) for j in range(i + 1)]
        triangle.append(row)
    
    return triangle
