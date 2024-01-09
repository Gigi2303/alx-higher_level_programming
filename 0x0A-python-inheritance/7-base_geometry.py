#!/usr/bin/python3
"""
This module contaions  class that creates a class BaseGeometry
    (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """ This is aclass baseGeometry """
    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates values

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
