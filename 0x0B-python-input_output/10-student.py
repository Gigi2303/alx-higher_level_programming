#!/usr/bin/python3

"""
This contains a class that defines a student with their details.
"""


class Student:
    """This class defines a student

    Attributes:
        first_name: The first name of the student
        last_name: The last name of the student
        age: The student's age
        __init__(self, first_name, last_name, age)
        to_json(self, attrs=None)
    """

    def __init__(self, first_name, last_name, age):
        """Initializes the class instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student

        Return: a dictionary conatining instance details
        """
        if (type(attrs) is list and
                all(type(geh) is str for geh in attrs)):
            return {g: getattr(self, g) for g in attrs if hasattr(self, g)}
        return self.__dict__
