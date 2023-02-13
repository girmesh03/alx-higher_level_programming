#!/usr/bin/python3
""" Test cases for the Base class. """

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestBase(unittest.TestCase):
    """
    TestCase class for the Base class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        Base._Base__nb_objects = 0

    def test_base_creation(self):
        """
        Test the creation of Base objects.
        """
        obj1 = Base()
        self.assertIsInstance(obj1, Base)
        self.assertEqual(obj1.id, 1)

        obj2 = Base()
        self.assertIsInstance(obj2, Base)
        self.assertEqual(obj2.id, 2)

        obj3 = Base(10)
        self.assertIsInstance(obj3, Base)
        self.assertEqual(obj3.id, 10)

        obj4 = Base()
        self.assertIsInstance(obj4, Base)
        self.assertEqual(obj4.id, 3)

    def test_base_number_of_arguments(self):
        """
        Raise a TypeError if the number of arguments is not 1.
        """
        with self.assertRaises(TypeError):
            obj1 = Base(1, 2)

    def test_private_attribute(self):
        """
        Test that the private attributes are not accessible.
        """
        obj1 = Base()
        with self.assertRaises(AttributeError):
            obj1.__nb_objects

    def test_to_json_string(self):
        """
        Test the to_json_string method.
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')
        self.assertEqual(Base.to_json_string([{'id': 1}, {'id': 2}]),
                         '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        """
        Test the from_json_string method.
        """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{'id': 1}])
        self.assertEqual(Base.from_json_string('[{"id": 1}, {"id": 2}]'),
                         [{'id': 1}, {'id': 2}])

    def test_save_to_file_1(self):
        """ Test JSON file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
