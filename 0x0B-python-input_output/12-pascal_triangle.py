#!/usr/bin/python3

"""
This contains a function that returns a pascal's triangle
"""


def pascal_triangle(n):
    """Return a list of lists of integers representing
    pascal's triangle

    Args:
        n: length of the triangle
    """
    if n <= 0:
        return []
    else:
        row = [[1] for i in range(n)]
        for g in range(1, n):
            for h in range(g):
                try:
                    prev = row[g - 1][h + 1]
                except IndexError:
                    prev = 0
                row[g].append(prev + row[g-1][h])
        return row
