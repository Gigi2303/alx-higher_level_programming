#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    11 = len(tuple_a)
    12 = len(tuple_b)
    avalue_1 = tuple_a[0] if 11 > 0 else 0
    avalue_2 = tuple_a[1] if 11 > 1 else 0
    bvalue_1 = tuple_b[0] if 12 > 0 else 0
    bvalue_2 = tuple_b[1] if 12 > 1 else 0

    return ("{}".format((avalue_1 + bvalue_1, avalue_2 + bvalue_2)))
