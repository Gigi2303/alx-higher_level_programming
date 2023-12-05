#!/usr/bin/python3

def no_c(my_string):
    copy_ = ""
    for g in my_string:
        if g == 'c' or g == 'C':
            copy_ += ""
        else:
            copy_ += g
    return copy_
