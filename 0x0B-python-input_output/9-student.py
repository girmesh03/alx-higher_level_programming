#!/usr/bin/python3
"""A module that defines a Student class"""


class Student:
    """This class defines a student by: first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        """A constructor for the Student class

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A method that retrieves a dictionary representation of a Student
        instance

        Returns:
            A dictionary representation of a Student instance
        """
        return self.__dict__
