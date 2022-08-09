#!/usr/bin/python3
"""
Unittest module for the Amenity Class.
"""

import unittest
import pycodestyle
from models.amenity import Amenity
from models import amenity
from models.base_model import BaseModel


class TestAmenityDocs(unittest.TestCase):
    """
    Implements tests for the base class

    The test checks if the base_model file conforms to pep8
    and the correct documentation

    Methods
    -------
    test_base_model(self)
        Run pycodestyle tests
    """

    def test_amenity_model(self):
        """ checks if the base_model file conforms to pep8 style """
        style = pycodestyle.Checker("models/amenity.py", show_source=True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 error and Warnings")

    def test_amenity_model_test(self):
        """ Tests this file for PEP8 errors"""

        style = pycodestyle.Checker("tests/test_models/test_amenity.py",
                                    show_source=True)
        results = style.check_all()
        self.assertEqual(results, 0, "Found PEP 8 errors & Warnings")

    def test_module_doc_string(self):
        """ Checks if the doc string is present"""

        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs documentation")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py need doc string")

    def test_class_doc_string(self):
        """ Tests if the class doc string exists"""

        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs doc str")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs doc str")


class TestAmenity(unittest.TestCase):

    """
    Test Cases for the Amenity class.

    Methods
    -------
    test_amenity_instantiation
        Checks for correctness in initialization
    test_amenity_attributes
        checks for attributes correctness
    """

    def test_amenity_instantiation(self):
        """
        Tests instantiation of Amenity class.
        """

        my_amenity = Amenity()
        self.assertEqual(str(type(my_amenity)),
                         "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(my_amenity, Amenity)
        self.assertTrue(issubclass(type(my_amenity), BaseModel))

    def test_amenity_attributes(self):
        """
        Tests the attributes of Amenity class.
        """

        my_amenity = Amenity()
        attributes = my_amenity.to_dict()
        for k, v in attributes.items():
            self.assertTrue(hasattr(my_amenity, k))
            self.assertEqual(my_amenity.__dict__[k], v)


if __name__ == "__main__":
    unittest.main()
