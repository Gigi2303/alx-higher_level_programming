#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for g in a_dictionary:
        new_dictionary[g] = a_dictionary[g] * 2
    return new_dictionary
