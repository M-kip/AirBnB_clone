#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
import pycodestyle
from models.place import Place
from models import place
from models.base_model import BaseModel


class TestPlaceDocs(unittest.TestCase):
    """
    Runs Doc string and pycodestyle checks

    This class checks for proper code documentation
    if the class/ module contains __doc__ strings

    Methods
    -------
    test_place_pep8(self)
        Run checks with pycodestyle
    test_place_module_doc_string(self)
        Checks for module doc string
    test_place_class_doc_string(self)
        Checks for class doc strings
    test_place_test_pep8(self)
        Tests this script for pep compliance
    """

    def test_place_pep8(self):
        """
        Checks for PEP 8 compliance
        """
        style = pycodestyle.Checker("models/place.py", show_source=True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 Warnings")

    def test_place_test_pep8(self):
        """
        Checks for PEP 8 compliance
        """
        style = pycodestyle.Checker("tests/test_models/test_place.py",
                                    show_source=True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 Warnings")

    def test_module_doc_string(self):
        """ Checks if the doc string is present"""

        self.assertIsNot(place.__doc__, None, "place.py needs documentation")
        self.assertTrue(len(place.__doc__) >= 1, "place.py need doc string")

    def test_class_doc_string(self):
        """ Tests if the class doc string exists"""

        self.assertIsNot(Place.__doc__, None, "Place class needs doc str")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs doc str")


class TestPlace(unittest.TestCase):

    """
    Test Cases for the Place class.

    Tests module/class/variables for correctness (logic & syntax)

    Methods
    -------
    test_place_instantiation(self)
        checks if Place class instantiation is correct
    test_place_attributes(self)
        test correctness of attributes
    """

    def test_place_instantiation(self):
        """
        Tests instantiation of Place class.

        Raises
        ------
        NotInstanceError
            if not instance of Place
        NotTrueError
            raises this error if instance not a subclass of BaseModel
        """

        my_place = Place()
        self.assertEqual(str(type(my_place)), "<class 'models.place.Place'>")
        self.assertIsInstance(my_place, Place)
        self.assertTrue(issubclass(type(my_place), BaseModel))

    def test_place_attributes(self):
        """
        Tests the attributes of Place class.

        Raises
        ------
        NotTrueError
            if instance doesn't have a variables
        NotEqualError
            if instance values don't match with test values
        """

        my_place = Place()
        attributes = my_place.to_dict()
        for k, v in attributes.items():
            self.assertTrue(hasattr(my_place, k))
            self.assertEqual(attributes[k], v)


if __name__ == "__main__":
    unittest.main()
