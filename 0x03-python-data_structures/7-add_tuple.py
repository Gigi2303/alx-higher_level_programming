#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    t1 = len(tuple_a)
    t2 = len(tuple_b)
    avalue_1 = tuple_a[0] if t1 > 0 else 0
    avalue_2 = tuple_a[1] if t1 > 1 else 0
    bvalue_1 = tuple_b[0] if t2 > 0 else 0
    bvalue_2 = tuple_b[1] if t2 > 1 else 0

    return ("{}".format((avalue_1 + bvalue_1, avalue_2 + bvalue_2)))
