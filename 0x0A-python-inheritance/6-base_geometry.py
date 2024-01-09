#!/usr/bin/python3

"""
This module contains a class that creates a base geometry
"""


class BaseGeometry:
    """This creates an empty class BaseGeometry
        with public instance method area

    Attributes:
        area(self) - The area of the base geometry
    Raise:
        Exception
    """
    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")
