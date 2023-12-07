#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_ = list(map(lambda row: list(map(lambda g: g ** 2, row)), matrix))
    return squared_
