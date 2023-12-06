#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for gb in a_dictionary:
        new_dictionary[gb] = a_dictionary[gb] * 2
    return new_dictionary
