#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    tt = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    dic = {"+": add, "-": sub, "*": mul, "/": div}

    if tt not in dic:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {:s} {:d} = {:d}".format(a, tt, b, dic[tt](a, b)))
