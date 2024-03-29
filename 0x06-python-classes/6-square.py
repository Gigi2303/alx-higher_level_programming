#!/usr/bin/python3
"""This module defines a square byPrivate instance attribute: size
    property def size(self): to retrieve it and
    property setter def size(self, value): to set it
    Public instance method: def my_print(self)
"""

class Square():
                """This class defines a square with private instance size"""
        def __init__(self, size=0, position=(0, 0)):
            self.size =  size
            self.position = position

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
        @property
        def position(self):
            return self.__position

        @position.setter
        def position(self, value):
            if not isinstance(value, tuple) or len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
            elif not all(isinstance(num, int) and num >= 0 for num in value):
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = value

        def area(self):
                return self.__size ** 2

        def my_print(self):
            if self.__size == 0:
                print()
            else:
                for _ in range (self.__position[1]):
                    print()
                for _ in range(self.__size):
                    print(" " * self.__position[0] + "#" * self.__size)
