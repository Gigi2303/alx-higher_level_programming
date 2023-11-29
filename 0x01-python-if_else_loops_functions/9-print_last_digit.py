#!/usr/bin/python3

def print_last_digit(number):

    if number < 0:
        number = number * (-1)
        lama = (number % 10)
    print("{}".format(lama), end="")
    return (lama)
