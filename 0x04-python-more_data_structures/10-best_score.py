#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        best = max(list(a_dictionary.values()))
        for g in a_dictionary:
            if a_dictionary[g] == best:
                return g
    return None
