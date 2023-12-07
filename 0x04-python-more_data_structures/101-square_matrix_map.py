#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda g: list(map(lambda b: b**2, g)), matrix))
