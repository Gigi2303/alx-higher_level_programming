#!/usr/bin/python3

class Square():
    """This class defines a square with private instance size"""
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size
