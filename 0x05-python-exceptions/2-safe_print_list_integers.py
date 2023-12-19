#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_integer = 0
    
    try:
        for bufa in my_list[:x]:
            print("{:d}".format(value), end=" ")
            printed_integer += 1

        except (IndexError, ValueError, TypeError):
            pass

        print("")

        return printed_integer
