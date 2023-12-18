#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_length = 0

    try:
        for g in range(x):
            print("{}".format(my_list[printed_length]), end="")
            printed_length += 1
    except IndexError:
        pass
    
    finally:
        print("")

        return printed_length
