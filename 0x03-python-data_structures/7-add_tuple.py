#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    21 = len(tuple_a)
    32 = len(tuple_b)
    avalue_1 = tuple_a[0] if 21 > 0 else 0
    avalue_2 = tuple_a[1] if 21 > 1 else 0
    bvalue_1 = tuple_b[0] if 32 > 0 else 0
    bvalue_2 = tuple_b[1] if 32 > 1 else 0

    return ("{}".format((avalue_1 + bvalue_1, avalue_2 + bvalue_2)))
