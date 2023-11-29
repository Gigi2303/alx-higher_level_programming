#!/usr/bin/python3

for x in range(122, 96, -1):
    print("{}".format(
        chr(x).lower() if x % 2 == 0 else chr(x).upper()
        ), end="")
