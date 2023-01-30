#!/usr/bin/python3

"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A class that contains all the test cases for max_integer()"""

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_none(self):
        """Test None"""
        self.assertIsNone(max_integer())

    def test_ordered_list(self):
        """Test ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        """Test one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_at_beginning(self):
        """Test at beginning"""
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)

    def test_at_end(self):
        """Test at end"""
        self.assertEqual(max_integer([1, 2, 3, 5]), 5)

    def test_int_float(self):
        """Test int and float"""
        self.assertEqual(max_integer([1, 2.2, 3, 4]), 4)

    def test_negative(self):
        """Test negative"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_float(self):
        """Test float"""
        self.assertEqual(max_integer([1.1, 4.8, 3.3, 2.2]), 4.8)

    def test_string(self):
        """Test string"""
        self.assertEqual(max_integer("Hello"), "o")

    def test_empty_string(self):
        """Test empty string"""
        self.assertIsNone(max_integer(""))

    def test_list_of_strings(self):
        """Test list of strings"""
        self.assertEqual(max_integer(["Hello", "World"]), "World")

    def test_list_of_lists(self):
        """Test list of lists"""
        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])

    def test_list_of_tuples(self):
        """Test list of tuples"""
        self.assertEqual(max_integer([(1, 2), (3, 4)]), (3, 4))


if __name__ == '__main__':
    unittest.main()
