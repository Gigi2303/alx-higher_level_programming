#!/usr/bin/python3

def uppercase(str):

    lov = ""

    for g in str:

        if ord(g) >= 97 and ord(g) <= 122:
            lov += chr(ord(g) - 32)
        else:
            lov += g

    print("{}".format(lov), end="\n")
