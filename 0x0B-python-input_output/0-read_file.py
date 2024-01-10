#!/usr/bin/python3

"""
A function that  reads a text file (UTF8) and prints it to stdout
Prototype: def read_file(filename="")

"""

def read_file(filename=""):
    """
    This function opens and reads file and print to stdout
    Argument:
            filename
    """
     with open(filename, "r", encoding="utf-8") as g:
        print(g.read(), end="")
