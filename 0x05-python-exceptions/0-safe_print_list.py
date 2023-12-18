#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_length = 0

    while printed_length < x:
        try:
            print("{}".format(my_list[printed_length]), end="")
        except IndexError:
            break
        printed_length += 1
    print("")

    return printed_length
