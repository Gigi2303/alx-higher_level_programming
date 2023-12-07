#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_set = set()
    for g in my_list:
        unique_set.add(g)
    sum_unique = sum(unique_set)
    return sum_unique
