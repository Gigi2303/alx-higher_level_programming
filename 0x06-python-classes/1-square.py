#!/usr/bin/python3

"""This is a module that Write a class Square that defines a square by
    private instance size
"""
class Square():
    """This class defines a square with private instance size"""
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size
