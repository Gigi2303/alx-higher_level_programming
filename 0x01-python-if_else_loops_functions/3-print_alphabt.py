#!/usr/bin/python3
for g in range(97, 123):
    if (g == 101) or (g == 113):
        continue
    print("{}".format(chr(g)), end="")
