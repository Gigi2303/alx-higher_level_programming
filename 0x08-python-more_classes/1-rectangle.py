#!/usr/bin/python3

"""
This is a module that contains a class that defines a Rectangle with
private attribute width.
"""

class Rectangle:
    """This is a class that defines a rectangle

    Attributes:
        width: The width of rectangle
        height: The height of rectangle
        __init__(self, width=0, height=0)

    Raise:
        TypeError: width must be an integer
        ValueError: width must be >= 0
    """

    def __init__(self, width=0, height=0):
        """This method initializes the class instance

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
         """This method retrieves the width of the rectangle

        Return: The width
        """
        return self._width

    @width.setter
    def width(self, value):
        """This is a method that set the new value of the width

        Args:
            value: The new width
        Raise:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """This is a method that retrieves the height of the rectangle

        Return: The height
        """
        return self._height

    @height.setter
    def height(self, value):
        """This is a method that set the new value of the height

        Args:
            value: The new height
        Raise:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

       else:
           if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

