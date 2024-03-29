#!/usr/bin/python3
"""This module Write a class Square that defines a square by
Instantiation with optional size
"""
class Square():
        """This class defines a square with private instance size"""
        def __init__(self, size=0):
            if not isinstance (size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

        def get_size(self):
            return self.__size

