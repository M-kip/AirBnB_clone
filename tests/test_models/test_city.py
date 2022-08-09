#!/usr/bin/python3
"""Unittest module for the City Class.
"""

import unittest
import pycodestyle
from models.city import City
from models import city
from models.base_model import BaseModel


class TestCityDocs(unittest.TestCase):
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
        style = pycodestyle.Checker("models/city.py", show_source=True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 Warnings")

    def test_place_test_pep8(self):
        """
        Checks for PEP 8 compliance
        """
        style = pycodestyle.Checker("tests/test_models/test_city.py",
                                    show_source=True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 Warnings")

    def test_module_doc_string(self):
        """ Checks if the doc string is present"""

        self.assertIsNot(city.__doc__, None, "city.py needs documentation")
        self.assertTrue(len(city.__doc__) >= 1, "city.py need doc string")

    def test_class_doc_string(self):
        """ Tests if the class doc string exists"""

        self.assertIsNot(City.__doc__, None, "City class needs doc str")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs doc str")


class TestCity(unittest.TestCase):
    """
    Test Cases for the City class.
    """

    def test_city_instantiation(self):
        """
        Tests instantiation of City class.
        """

        my_city = City()
        self.assertEqual(str(type(my_city)), "<class 'models.city.City'>")
        self.assertIsInstance(my_city, City)
        self.assertTrue(issubclass(type(my_city), BaseModel))

    def test_city_attributes(self):
        """
        Tests the attributes of City class.
        """

        my_city = City()
        attributes = my_city.to_dict()
        for k, v in attributes.items():
            self.assertTrue(hasattr(my_city, k))
            self.assertEqual(my_city.__dict__[k], v)


if __name__ == "__main__":
    unittest.main()
