#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    _list_copy = my_list[:]
    if idx >= len(_list_copy) or idx < 0:
        return _list_copy
    _list_copy[idx] = element
    return _list_copy
