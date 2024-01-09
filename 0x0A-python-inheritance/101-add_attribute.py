#!/usr/bin/python3

"""
This module contains a class MyInt that inherits from int
"""


def add_attribute(obj, attr, value):
    """Adds attribute to an object if possible

    Args:
        obj: The object to which new attribute is
        to be added
        attr: Attribute to be added
        value: The corresponding attribute value

    Raise:
        TypeError
    """

    if hasattr(obj, '__dict__'):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
