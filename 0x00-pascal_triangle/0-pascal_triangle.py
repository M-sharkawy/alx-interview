#!/usr/bin/python3
"""
pascal triangle 
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    Triangle = []
    if n <= 0:
        return Triangle
    Triangle = [[1]]
    for i in range(1, n):
        prev = Triangle[- 1]
        temp = [1]
        for j in range(1, i):
            temp.append(prev[j - 1] + prev[j])
        temp.append(1)
        Triangle.append(temp)
    return Triangle
