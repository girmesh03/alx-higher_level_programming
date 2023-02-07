#!/usr/bin/python3
"""A module that contains a class Student"""


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

    def to_json(self, attrs=None):
        """A method that retrieves a dictionary representation of a Student
        instance

        Args:
            attrs (list): A list of attributes to retrieve

        Returns:
            A dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict

    def reload_from_json(self, json):
        """A method that replaces all attributes of the Student instance

        Args:
            json (dict): A dictionary of attributes to replace the Student
            instance's attributes with
        """
        for key, value in json.items():
            self.__dict__[key] = value
