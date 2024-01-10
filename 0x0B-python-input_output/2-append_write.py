#!/usr/bin/python3

"""This is a function that appends a string
at the end of a text file (UTF8) and returns
the number of characters added
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text
        file (UTF8) and returns the number of characters added
        Args:
            filename (str): name of the file
            text (str): what to write
        Returns:
            int: number of characters written
    """

    with open(filename, "a", encoding="utf-8") as g:
        numb = g.write(text)

    return numb
