#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_integer = 0
    
    for bufa in my_list[:x]:
        try:
            print("{:d}".format(bufa), end="")

        except (ValueError, TypeError):
            continue
        printed_integer += 1

    print("")

    return printed_integer
