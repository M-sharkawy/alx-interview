#!/usr/bin/env python3

''' Pascal's Triangle module'''


def pascal_triangle(n):
    """Returns a list of lists representing Pascal triangle of n"""
    list = []
    if n <= 0:
        return list
    else:
        triangle = [[1]]
        for i in range(1, n):
            prev = triangle[-1]
            row = [1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
            triangle.append(row)
        return triangle
