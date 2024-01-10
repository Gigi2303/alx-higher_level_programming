#!/usr/bin/python3

"""This Contains function that writes a string 
to a text file (UTF8) and returns the number of characters written

"""
def write_file(filename="", text=""):
    """
    This is a function that writes a string to a text file (UTF8)
    Argument:
            filename - The name of the file to write in
            text - The text to be written
    """
    with open(filename, "w", encoding="UTF8") as g:
        numb = g.write(text)
        return numb
