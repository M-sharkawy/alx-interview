#!/usr/bin/python3
'''model to print single character'''

from copy import copy

def minOperations(n: int) -> int:
    """minimum operation to execute n numbers"""
    if n < 2:
        return 0

    operations = 0
    i = 2

    while n > 1:
        while n % i == 0:
            operations += i
            n //= i
        i += 1

    return operations
