#!/usr/bin/python3

"""
Contains function that return an object(Python data structure)
representation by a JSON string.
"""


def from_json_string(my_str):
    """This returns python data structure by a JSON string

    Args:
        my_str: JSON string to return object from
    """
    import json

    return json.loads(my_str)
