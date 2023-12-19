#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    rack = 0
    for atg in range(x):
        try:
            print("{:d}".format(my_list[atg]), end="")
        except (ValueError, TypeError):
            continue
        rack += 1
    print("")
    return rack
