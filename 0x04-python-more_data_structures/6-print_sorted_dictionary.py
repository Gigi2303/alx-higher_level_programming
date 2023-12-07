#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for g in sorted(a_dictionary):
        print("{}: {}".format(g, a_dictionary[g]))
