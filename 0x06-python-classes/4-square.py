#!/usr/bin/python3
"""This module defines a square byPrivate instance attribute: size
    property def size(self): to retrieve it and
    property setter def size(self, value): to set it
"""

class Square():
                """This class defines a square with private instance size"""
        def __init__(self, size=0):
            self.size =  size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance (value, int):
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

        def area(self):
                return self.__size ** 2
