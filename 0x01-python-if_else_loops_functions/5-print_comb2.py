#!/usr/bin/python3

for t in range(0, 100):
    if t != 99:
        print("{:02d}".format(t), end=", ")
    else:
        print("{:02d}".format(t), end="\n")
