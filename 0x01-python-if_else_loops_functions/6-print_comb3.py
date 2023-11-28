#!/usr/bin/python3
for x in range(9):
    for y in range(x + 1, 10):
        if x < 8:
            print("{}{}".format(x % 10, y % 10), end=", ")
        else:
            print("{}{}".format(x % 10, y % 10), end="\n")
